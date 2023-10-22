from bs4 import BeautifulSoup
import requests, re

data = requests.get("https://www.scrapethissite.com/pages/simple/").content
soup = BeautifulSoup(data, 'html.parser')
div = soup.find("h3", {"class":"country-name"})
country = div.text
span = soup.find("span", {"class":"country-population"})
population = span.text
print("Country %s has a population of %s" % (country, population))
