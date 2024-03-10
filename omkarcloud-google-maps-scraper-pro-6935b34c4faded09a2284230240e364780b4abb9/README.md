![Google Maps Scraper Feautred Image](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/google-maps-scraper-feautred-image.png)

<div align="center" style="margin-top: 0;">
  <h1>✨ Google Maps Scraper 🤖</h1>
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="google-maps-scraper forks" src="https://img.shields.io/github/forks/omkarcloud/google-maps-scraper?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://img.shields.io/github/stars/omkarcloud/google-maps-scraper?style=for-the-badge&color=yellow" />
  </a>
  <a href="#">
    <img alt="google-maps-scraper License" src="https://img.shields.io/github/license/omkarcloud/google-maps-scraper?color=orange&style=for-the-badge" />
  </a>
  <a href="https://github.com/omkarcloud/google-maps-scraper/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/omkarcloud/google-maps-scraper?color=purple&style=for-the-badge" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/google-maps-scraper.svg" width="80px" height="28px" alt="View" />
</p>

<p align="center">
  <a href="https://gitpod.io/#https://github.com/omkarcloud/google-maps-scraper">
    <img alt="Open in Gitpod" src="https://gitpod.io/button/open-in-gitpod.svg" />
  </a>
</p>
  
---

## Disclaimer for Google Maps Scraper Project

> This Google Maps Scraper is provided for educational and research purposes only. By using this Google Maps Scraper, you agree to comply with local and international laws regarding data scraping and privacy. The authors and contributors are not responsible for any misuse of this software. This tool should not be used to violate the rights of others, for unethical purposes, or to use data in an unauthorized or illegal manner.

We take the concerns of the Google Maps Scraper Project very seriously. For any concerns, please contact Chetan Jain at [chetan@omkar.cloud](mailto:chetan@omkar.cloud). We will promptly reply to your emails.

##  Explore Our Other Awesome Products

- ✅ [BOTASAURUS](https://github.com/omkarcloud/botasaurus): The All-in-One Web Scraping Framework with Anti-Detection, Parallelization, Asynchronous, and Caching Superpowers.

- ✅ [GOOGLE SCRAPER](https://github.com/omkarcloud/google-scraper): Discover Search Results from Google.

- ✅ [AMAZON SCRAPER](https://github.com/omkarcloud/amazon-scraper): Discover Search Results and Product Data from Amazon.

- ✅ [TRIP ADVISOR SCRAPER](https://github.com/omkarcloud/tripadvisor-scraper): Discover search results of hotels and restaurants from TripAdvisor.

---

Google Maps Scraper helps you find Business Profiles from Google Maps.

## ⚡ Benefits

1. Limitless Scraping, Say No to costly subscriptions or expensive pay-per-result fees.

2. Sort, select, and filter results.

3. Scrape cities across countries.

In the next 5 minutes, you'll extract **120 Search Results** from Google Maps.

![Google Maps Data Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/gmap_result.png)

## 🎥 Video Demo

If you'd like to see a demo before using the tool, I encourage you to watch this short video.

[![Google Maps Video Tutorial](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/video.png)](https://www.youtube.com/watch?v=6UZhTlkCb9A)


## 📦 Requirements

To use the tool, you must have Node.js 16+ and Python 3.8+ installed on your PC.

## 🚀 Getting Started

Let's get started by following these super simple steps:

1️⃣ Clone the Magic 🧙‍♀️:
```shell
git clone https://github.com/omkarcloud/google-maps-scraper
cd google-maps-scraper
```
2️⃣ Install Dependencies 📦:
```shell
python -m pip install -r requirements.txt
```
3️⃣ Get the results by running 😎

:
```shell
python main.py
```

Once the scraping process is complete, you will find the search results in the `output` directory.

![Google Maps Data Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/gmap_result.png)

*Note: If you don't have Node.js and Python installed or you are facing errors, follow this Simple FAQ [here](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-i-dont-have-python-or-im-facing-errors-when-setting-up-the-scraper-on-my-pc-how-to-solve-it), and you will have your search results in the next 5 Minutes*


## 🤔 Questions

### ❓ How to Scrape a Specific Search Query?
Open the `main.py` file, and update the `queries` list with your desired query.

```python
queries = ["web developers in delhi"]
Gmaps.places(queries, max=5)
```

### ❓ How to Scrape Multiple Queries?
Add multiple queries to the `queries` list as follows:

```python
queries = [
   "web developers in bangalore",
   "web developers in delhi",
]
Gmaps.places(queries, max=5)
```

### ❓ The scraper is only retrieving 5 results. How can I scrape all Google Maps search results?
A: Remove the `max` parameter.

By doing so, you can scrape all the Google Maps Listing. For example, to scrape all web developers in Bangalore, modify the code as follows:
```python
queries = ["web developers in bangalore"]
Gmaps.places(queries)
```

You can scrape a maximum of 120 results per search, as Google does not display any more search results beyond that. However, don't worry about running out of results as there are thousands of cities in our world :).

### ❓ How Can I Filter Google Map Search Results?
You can apply filters such as:

1. `min_reviews`/`max_reviews` (e.g., 10)
2. `category_in` (e.g., "Dental Clinic", "Dental Laboratory")
3. `has_website` (e.g., True/False)
4. `has_phone` (e.g., True/False)
5. `min_rating`/`max_rating` (e.g., 3.5)

For instance, to scrape listings with at least 5 reviews and no more than 100 reviews, with a phone number but no website:

```python
Gmaps.places(queries, min_reviews=5, max_reviews=100, has_phone=True, has_website=False)
```

To scrape listings that belong to specific categories:

```python
Gmaps.places(queries, category_in=[Gmaps.Category.DentalClinic, Gmaps.Category.DentalLaboratory])
```

See the list of all supported categories [here](https://github.com/omkarcloud/google-maps-scraper/blob/master/categories.md)

### ❓ How to Sort by Reviews, Rating, or Category?
We sort the listings using a really good sorting order, which is as follows:
  - Reviews [Businesses with more reviews come first]
  - Website [Businesses more open to technology come first]
  - LinkedIn [Businesses that are easier to contact come first]
  - Is Spending On Ads [Businesses already investing in ads are more likely to invest in your product, so they appear first.]

However, you also have the freedom to sort them according to your preferences as follows:

- To sort by reviews:

  ```python
  Gmaps.places(queries, sort=[Gmaps.SORT_BY_REVIEWS_DESCENDING])
  ```

- To sort by rating:

  ```python
  Gmaps.places(queries, sort=[Gmaps.SORT_BY_RATING_DESCENDING])
  ```

- To sort first by reviews and then by those without a website:

  ```python
  Gmaps.places(queries, sort=[Gmaps.SORT_BY_REVIEWS_DESCENDING, Gmaps.SORT_BY_NOT_HAS_WEBSITE])
  ```

- To sort by name (alphabetically):

  ```python
  Gmaps.places(queries, sort=[Gmaps.SORT_BY_NAME_ASCENDING])
  ```

- To sort by a different field, such as category, in ascending order:

  ```python
  Gmaps.places(queries, sort=[[Gmaps.Fields.CATEGORIES, Gmaps.SORT_ASCENDING]])
  ```

- Or, to sort in descending order:

  ```python
  Gmaps.places(queries, sort=[[Gmaps.Fields.CATEGORIES, Gmaps.SORT_DESCENDING]])
  ```
### ❓ How to Scrape Additional Information like Website, Phone, Geo Coordinates, Price Range?

You may upgrade to the Pro Version of the Google Maps Scraper to scrape additional data points, like:

- 🌐 **Website**
- 📞 **Phone Numbers**
- 🌍 **Geo Coordinates**
- 💰 **Price Range**
- And **many more data points** like Owner details, Photos, About Section, and [many more](https://github.com/omkarcloud/google-maps-scraper/blob/master/fields.md)!

Below is a sample search result scraped by the Pro Version:

![Pro Result](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/paid-lead.png)

*View sample search results scraped by the Pro Version [here](https://drive.google.com/file/d/10qSpi0Jrh7546M1fakjfBbaAS2ImBr8k/view?usp=sharing)*

Also, see the list of fields scraped by Pro Version [here](https://github.com/omkarcloud/google-maps-scraper/blob/master/fields.md).

🔍 **Comparison**:

See how the Pro Version stacks up against the free version in this comparison image:

![Comparison Image](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/comparision-image.png)

And here's the best part - the Pro Version comes with zero risk. That's right because we offer a **30-Day Refund Policy**!

Also, Pro Version is not a Monthly Subscription but a One Time Risk-Free Investment Only. 

### ❓ How to Get the Pro Version?

Visit the Sponsorship Page [here](https://github.com/sponsors/omkarcloud?frequency=one-time) and pay $28 by selecting Google Maps Scraper Pro Option.

![Pay](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/pay.gif)

After payment, you'll see a success screen with instructions on how to use the Pro Version:

![Success Screen](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/success-screen.png)

### ❓ What if I Don't Get Value from It?

We wholeheartedly believe in the value our product brings, especially since it has successfully worked for hundreds of people like you.
 
But, we also understand the reservations you might have.

That's why we've put the ball in your court: If, within the next 30 days, you feel that our product hasn’t met your expectations, don't hesitate. Reach out to us, and within 24 hours, we will gladly refund your money, no questions and no hassles.

The risk is entirely on us because we're confident in what we've created.

### ❓ How Do I Get a Refund?

We are ethical and honest people, and we will never keep your money if you are not happy with our product. Requesting a refund is a simple process that should only take about 5 minutes. To request a refund, ensure you have one of the following:

- **A PayPal Account (e.g., "myname@example.com" or "chetan@gmail.com")**
- **or a UPI ID (For India Only) (e.g., 'myname@bankname' or 'chetan@okhdfc')**

Next, follow these steps to initiate a refund:

1. Send an email to `chetan@omkar.cloud` using the following template:

   - To request a refund via PayPal:
     ```
     Subject: Request Refund
     Content: Please send a refund to my PayPal email: myname@example.com
     ```

   - To request a refund via UPI (For India Only):
     ```
     Subject: Request Refund
     Content: Please send a refund to my UPI ID: myname@bankname
     ```

   ![Email Image](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/email.png)

2. Next, go to the discussion [here](https://github.com/omkarcloud/google-maps-scraper/discussions/44) and comment to request a refund using this template:
   ```
   I have sent a refund request from my email: myname@example.com.
   ```

   ![Discussion Image](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/discussion.png)

3. You can expect to receive your refund within 1 day. We will also update you in the GitHub Discussion [here](https://github.com/omkarcloud/google-maps-scraper/discussions/44) :)

   ![PayPal Image](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/paypal.png)

All $28 will be refunded to you within 24 hours, without any questions and without any hidden charges.

### ❓ How Do I Scrape Social Details of Profiles like Email, Facebook, Twitter, etc.?

To scrape social details of profiles, follow these steps to use our Website Social Scraper API with the Free Plan, allowing you to scrape contact details of 50 profiles at no cost:

1. Sign up on RapidAPI by visiting [this link](https://rapidapi.com/auth/sign-up).
   
![Sign Up on RapidAPI](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/sign-up.png)

2. Subscribe to the Free Plan by visiting [this link](https://rapidapi.com/Chetan11dev/api/website-social-scraper-api/pricing).

![Subscribe to Free Plan](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/subscribe.png)

3. Copy the API key.
![Copy the API Key](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/key.png)

4. Use it in the scraper as follows:
```python
queries = ["web developers in bangalore"]
Gmaps.places(queries, max=5, key="YOUR_API_KEY") 
```
5. Run the script, and you'll find emails, Facebook, Twitter, and LinkedIn details of the Business in your output file.
```bash
python main.py
```   

Please note that this feature is available in Both Free and Pro Versions.

The first 50 contact details are free. After that, you can upgrade to the Pro Plan to scrape 1,000 contacts for $9, which is affordable considering if you land just one B2B client, you could easily make hundreds of dollars, easily covering the investment.

> Disclaimer: This API should not be used for bulk automated mailing, for unethical purposes, or in an unauthorized or illegal manner.

### ❓ How to scrape all cities in my country?

Consider this example, to scrape web developers from 100 cities in India, use the following example:

```python
queries = Gmaps.Cities.India("web developers in")[0:100]
Gmaps.places(queries) 
```

After running the code, an `india-cities.json` file will be generated in the `output` directory with a list of all the Indian cities.

You can prioritize certain cities by editing the cities JSON file in the output folder and moving them to the top of the list.

We recommend scraping only 100 cities at a time, as countries like India have thousands of cities, and scraping them all could take a considerable amount of time. Once you've exhausted the outreach in 100 cities, you can scrape more.

See the list of all supported countries [here](https://github.com/omkarcloud/google-maps-scraper/blob/master/countries.md)

### ❓ Can I Interrupt the Scrape While It's Running?
Yes, you can. The scraper is smart like you and will resume from where it left off if you interrupt the process.

### ❓ How to select more fields? [For Pro Users Only]

Seeing a lot of fields can be intimidating, so we have only kept the most important fields in the output.

However, you can select from up to multiple fields.

Also, to select all the fields, use the following code:

```python
queries = [
   "web developers in bangalore"
]
Gmaps.places(queries, fields=Gmaps.ALL_FIELDS)
```

To select specific fields only, use the following code:
<!-- todo: use fields -->
```python
queries = [
   "web developers in bangalore"
]

fields = [
   Gmaps.Fields.PLACE_ID, 
   Gmaps.Fields.NAME, 
   Gmaps.Fields.MAIN_CATEGORY, 
   Gmaps.Fields.RATING, 
   Gmaps.Fields.REVIEWS, 
   Gmaps.Fields.WEBSITE, 
   Gmaps.Fields.PHONE, 
   Gmaps.Fields.ADDRESS,
   Gmaps.Fields.LINK, 
]

Gmaps.places(queries, fields=fields)
```

Please note that selecting more or fewer fields will not affect the scraping time; it will remain exactly the same. So, don't fall into the trap of selecting fewer fields thinking it will decrease the scraping time, because it won't. 

For examples of CSV/JSON formats containing all fields, you can download [this file](https://drive.google.com/file/d/10qSpi0Jrh7546M1fakjfBbaAS2ImBr8k/view?usp=sharing).

Also, see the list of all supported fields [here](https://github.com/omkarcloud/google-maps-scraper/blob/master/fields.md)

### ❓ Could you share resources that would be helpful to me, as I am sending personalized emails and providing useful services?

- I recommend reading [The Cold Email Manifesto](https://www.amazon.com/Cold-Email-Manifesto-pipeline-business-ebook/dp/B0B1DYNNSL) to learn how to write effective cold emails.

### ❓ Are There Other Sources of Profiles That I Can Use?

Also, if hotel and restaurant owners are your primary target audience, consider using TripAdvisor instead of Google Maps due to the lower competition.

Our TripAdvisor Scraper allows you to easily gather contact information and descriptions from TripAdvisor. 

See our [Tripadvisor Scraper here](https://github.com/omkarcloud/tripadvisor-scraper).

### ❓ How Does It Work?

For web scrapers interested in understanding how it works, you can read [this tutorial](https://www.omkar.cloud/botasaurus/docs/google-maps-scraping-tutorial/), where we walk you through the creation of a simplified version of a Google Maps Scraper.

### ❓ Your Scraper is Really Robust. I Tried Many Scrapers, Most Don't Work. How Did You Build It?

Thanks! We used Botasaurus, which is the secret behind our Google Maps Scraper.

It's a Web Scraping Framework that makes life easier for Web Scrapers.

Botasaurus handled the hard parts of our Scraper, such as:
   - Caching
   - Parallel and Asynchronous Scraping
   - Creation and Reuse of Drivers
   - Writing output to CSV and JSON files

If you are a Web Scraper, we highly recommend that you learn about Botasaurus [here](https://github.com/omkarcloud/botasaurus), because Botasaurus will really save you countless hours in your life as a Web Scraper.

<p align="center">
  <a href="https://github.com/omkarcloud/botasaurus">
  <img src="https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/mascot.png" alt="botasaurus" />
</a>
</p>

### ❓ Advanced Questions

Having read this page, you have all the knowledge needed to effectively utilize the tool.

You may choose to explore the following questions based on your interests:

#### For Knowledge

1. [Do I Need Proxies?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-do-i-need-proxies)
2. [Does Running a Scraper on a Bigger Machine Scrape Data Faster?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-does-running-scraper-on-bigger-machine-scrapes-data-faster)

#### For Technical Usage

1. [I Don't Have Python, or I'm Facing Errors When Setting Up the Scraper on My PC. How to Solve It?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-i-dont-have-python-or-im-facing-errors-when-setting-up-the-scraper-on-my-pc-how-to-solve-it)
2. [How to Scrape Reviews?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-how-to-scrape-reviews)
3. [What Are Popular Snippets for Data Scientists?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-what-are-popular-snippets-for-data-scientists)
4. [How to Change the Language of Output?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-how-to-change-the-language-of-output)
5. [I Have Google Map Places Links, How to Scrape Links?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-i-have-google-map-places-links-how-to-scrape-links)
6. [How to Scrape at Particular Coordinates and Zoom Level?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-how-to-scrape-at-particular-coordinates-and-zoom-level)
7. [When Setting the Lang Attribute to Hindi/Japanese/Chinese, the Characters Are in English Instead of the Specified Language. How to Transform Characters to the Specified Language?](https://github.com/omkarcloud/google-maps-scraper/blob/master/advanced.md#-when-setting-the-lang-attribute-to-hindijapanesechinese-the-characters-are-in-english-instead-of-the-specified-language-how-to-transform-characters-to-the-specified-language)


### ❓ Need More Help or Have Additional Questions?

For further help, contact us on WhatsApp. We'll be happy to help you out.

[![Contact Us on WhatsApp about Amazon Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918295042963&text=Hi,%20I%20would%20like%20to%20learn%20more%20about%20your%20products.)

## Love It? [Star It ⭐!](https://github.com/omkarcloud/google-maps-scraper)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

[![Stargazers for @omkarcloud/google-maps-scraper](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=omkarcloud&repo=google-maps-scraper)](https://github.com/omkarcloud/google-maps-scraper/stargazers)

## Made with ❤️ using [Botasaurus Web Scraping Framework](https://github.com/omkarcloud/botasaurus)
