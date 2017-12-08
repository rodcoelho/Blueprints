import requests
import bs4
import re

# Objective:
# Return name and value as key-value pairs for all 100 coins

url = 'https://coinmarketcap.com/'
r = requests.get(url)
text = r.text
soup = bs4.BeautifulSoup(text, 'html5lib')

# get HTML lines where the name is listed
#<a class="currency-name-container" href="/currencies/exchange-union/">Exchange Union</a>
coin_names_list = soup.findAll(
    name = "a",
    attrs = {
        "class": re.compile("currency-name-container")
    })

# get HTML lines where the value is listed
# <a href="/currencies/bitcoin/#markets" class="price" data-usd="16923.8" data-btc="1.0">$16,923.80</a>
price_list = soup.findAll(
    name = "a",
    attrs = {
        "class": re.compile("price")
    })

# there are other elements in the HTML file that have price in the attribute class name so we need to get rid of the first four elements
new_price_list = price_list[4:]

d = {}
for i in range(len(coin_names_list)):
    href_link_name = coin_names_list[i].get('href')
    clean_title_name = coin_names_list[i].text

    href_link_price = new_price_list[i].get('data-btc')
    clean_title_price = new_price_list[i].text
    d[clean_title_name] = clean_title_price