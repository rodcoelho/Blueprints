Scraping the Web
================

Have you ever wanted to use the information from a website? A lot of our favorite sites have public APIs - but many don't. The information is still out there though - we've just got to scrape for it.

[Coin Market Cap](http://www.coinmarketcap.com) is the gold standard for crypto-currency values. Unfortunately, they don't have an official API. Several people have built APIs for them using web scrapers - and they were showered in bitcoin, dogecoin, and pizza. Time to get in on the action!

Use pip3 to install requests and beautifulsoup4.

```
pip3 install requests  
pip3 install beautifulsoup4
```

#### Scrape Coin Market Cap

Use [this tutorial](http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python) as a guide to scraping using requests and bs4. This is for a different site and case, but you should skim and read enough of the code snippets to get the idea. Your code should return the name of currency and it's current value as key-value pairs for all 100 coins on the market.

The complete list should be ordered as they are ordered on the market.

#### Save it to a CSV

Now export your list to a CSV file and save it in the directory. Push it up!
