import json
import os
from hashlib import md5
from joblib import Parallel, delayed
from shutil import rmtree
from json.decoder import JSONDecodeError
from .decorators_utils import create_cache_directory_if_not_exists, create_directory_if_not_exists
from .utils import read_json, relative_path, write_json

class DontCache:
    def __init__(self, result):
        self.data = result

def is_dont_cache(obj):
    return isinstance(obj, DontCache)

def _get_cache_path(func, data):
    fn_name = func.__name__
    fn_cache_dir = f'cache/{fn_name}/'

    # Serialize the data to a JSON string and encode to bytes
    serialized_data = json.dumps(data).encode('utf-8')
    
    # Generate a hash from the serialized data
    data_hash = md5(serialized_data).hexdigest()

    # Create a unique cache file path with a .json extension
    cache_path = os.path.join(fn_cache_dir, data_hash + ".json")
    return cache_path

def _hash( data):
    # Serialize the data to a JSON string and encode to bytes
    serialized_data = json.dumps(data).encode('utf-8')
    
    # Generate a hash from the serialized data
    return  md5(serialized_data).hexdigest()


def _has(cache_path):
    return os.path.exists(cache_path)

def _get(cache_path):
    try:
        return read_json(cache_path)
    except JSONDecodeError:
        return None


def _read_json_files(file_paths):
    results = Parallel(n_jobs=-1)(delayed(_get)(file_path) for file_path in file_paths)
    return results

def _delete_item_by_path(cache_path):
    os.remove(cache_path)

def _delete_items(file_paths):
    Parallel(n_jobs=-1)(delayed(_delete_item_by_path)(file_path) for file_path in file_paths)

def _put(result, cache_path):
    write_json(result, cache_path)

def _remove(cache_path):
    if os.path.exists(cache_path):
        os.remove(cache_path)

def get_files_without_json_extension(directory_path):
    # Get a list of all files in the directory
    files = os.listdir(directory_path)
    
    # Use rstrip to remove the .json extension from all filenames in the list
    files_without_json_extension = [file.rstrip('.json') for file in files]
    
    return files_without_json_extension


created_fns = set()
cache_check_done = False


def _create_cache_directory_if_not_exists(func=None):
        global cache_check_done
        if not cache_check_done:
            cache_check_done = True
            create_cache_directory_if_not_exists()

        if func is not None: 
            fn_name = func.__name__
            
            if fn_name not in created_fns:
                created_fns.add(fn_name)
                fn_cache_dir = f'cache/{fn_name}/'
                create_directory_if_not_exists(fn_cache_dir)

class Cache:

    REFRESH = "REFRESH"
    
    @staticmethod
    def put(func, key_data, data):
        """Write data to a cache file in JSON format."""
        _create_cache_directory_if_not_exists(func)
        path = _get_cache_path(func, key_data)
        _put(data, path)

    @staticmethod
    def hash(data):
        return _hash(data)

    @staticmethod
    def filter_items_not_in_cache(func, items):
        cached_items  = set(Cache.get_items_hashes(func))
        return [item for item in items if Cache.hash(item) not in cached_items]
            

    @staticmethod
    def filter_items_in_cache(func, items):
        cached_items  = set(Cache.get_items_hashes(func))
        return [item for item in items if Cache.hash(item) in cached_items]
                        
    @staticmethod
    def has(func, key_data):
        _create_cache_directory_if_not_exists(func)
        path = _get_cache_path(func, key_data)
        return _has(path)

    @staticmethod
    def get(func, key_data):
        """Read data from a cache file."""
        _create_cache_directory_if_not_exists(func)
        path = _get_cache_path(func, key_data)
        if _has(path):
            return _get(path)
        return None


    @staticmethod
    def get_items(func, items=None):
        hashes = Cache.get_items_hashes(func, items)
        fn_name = func.__name__
        paths = [relative_path(f'cache/{fn_name}/{r}.json') for r in hashes]
        return _read_json_files(paths)

    @staticmethod
    def get_items_hashes(func, items=None):
        fn_name = func.__name__
        fn_cache_dir = f'cache/{fn_name}/'
        cache_dir = relative_path(fn_cache_dir)
        results =  get_files_without_json_extension(cache_dir)

        if items is None:
            return results
        else: 
            items  = set([Cache.hash(item) for item in items])
            return [r for r in results if r in items]

    @staticmethod
    def remove(func, key_data):
        """Remove a specific cache file."""
        _create_cache_directory_if_not_exists(func)
        path = _get_cache_path(func, key_data)
        _remove(path)

    @staticmethod
    def remove_items(func, items):

        """Remove a specific cache file."""
        hashes = Cache.get_items_hashes(func, items)
        fn_name = func.__name__
        paths = [relative_path(f'cache/{fn_name}/{r}.json') for r in hashes]
        _delete_items(paths)
        return len(hashes)

    @staticmethod
    def clear(func=None):
        """Clear all cache files. 
        If func is specified, clear cache for that specific function, 
        otherwise clear the entire cache directory."""
        global cache_check_done, created_fns

        if func is not None:
            fn_name = func.__name__
            fn_cache_dir = f'cache/{fn_name}/'
            cache_dir = relative_path(fn_cache_dir)
            if os.path.exists(cache_dir):
                rmtree(cache_dir, ignore_errors=True)
            if fn_name in created_fns:
                created_fns.remove(fn_name)
        else:
            cache_dir = relative_path('cache/')
            if os.path.exists(cache_dir):
                rmtree(cache_dir, ignore_errors=True)
            cache_check_done = False
            created_fns = set()



if __name__ == "__main__":

    # Test function to be cached
    def test_function(data):
        print(f"Processing data: {data}")
        return {"processed": data, "status": "success"}

    # Test data
    sample_data = {"key": "value"}

    # Test Case 1: Adding data to the cache
    Cache.put(test_function, sample_data, test_function(sample_data))
    print("Test Case 1: Data added to cache.")

    # Test Case 2: Checking if data exists in the cache
    if Cache.has(test_function, sample_data):
        print("Test Case 2: Data found in cache.")
    else:
        print("Test Case 2: Data not found in cache.")

    # Test Case 3: Retrieving data from the cache
    cached_data = Cache.get(test_function, sample_data)
    if cached_data:
        print(f"Test Case 3: Retrieved data from cache:", cached_data)
    else:
        print("Test Case 3: No data retrieved from cache.")

    # Test Case 4: Removing data from the cache
    Cache.remove(test_function, sample_data)
    if not Cache.has(test_function, sample_data):
        print("Test Case 4: Data removed from cache.")
    else:
        print("Test Case 4: Data still exists in cache.")

    # Test Case 5: Clearing the cache
    Cache.clear()
    print("Test Case 5: Cache cleared.")

    # Test Case 6: Retrieving data from the cache
    cached_data = Cache.get(test_function, sample_data)
    if cached_data:
        print(f"Test Case 6: Retrieved data from cache:", cached_data)
    else:
        print("Test Case 6: No data retrieved from cache.")

