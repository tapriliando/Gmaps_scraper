from src import Gmaps

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

queries = [
   "Perusahaan Rental di Palembang"
]

Gmaps.places(queries, max=5, fields=Gmaps.ALL_FIELDS)