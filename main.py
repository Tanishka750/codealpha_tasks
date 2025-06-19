import requests
from bs4 import BeautifulSoup
import pandas as pd

def my_web_scrapper(url):
  proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
    }

# def my_web_scrapper(url):
# url ="https://www.nykaa.com/makeup/lips/c/15?page_no=1&sort=popularity&search_redirection=True&eq=desktop"
# url ="https://www.nykaa.com/makeup/face/face-foundation/c/228?search_redirection=True"
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
  r = requests.get(url, headers=headers)

  soup=BeautifulSoup(r.text,'html.parser')

  data = {'Title': [], 'Price': []}

  spans=soup.select("div.css-xrzmfa")
# for span in spans:
#  print (span.string)
# data["Title"].append(span.get_text(strip=True))


  prices=soup.select("span.css-111z9ua")
# for price in prices:
#   print(price.string)
# data["price"].append(price.get_text(strip=True))
  num_items = min(len(spans), len(prices))

  for i in range(num_items):
      data["Title"].append(spans[i].string)
      data["Price"].append(prices[i].string)


  df=pd.DataFrame.from_dict(data)
  df.to_csv("data.csv", index=False)


 