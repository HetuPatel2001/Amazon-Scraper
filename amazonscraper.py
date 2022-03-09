from bs4 import BeautifulSoup   
import requests
import pandas as pd

item = input("What are you looking for?")
url = 'https://www.amazon.in/s?k=' + str(item)    
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.3'}
req = requests.get(url, headers = headers)
soup = BeautifulSoup(req.text, 'html.parser')


names=[]
for i in soup.find_all(class_="a-size-medium a-color-base a-text-normal"):
    names.append(i.text)
print(len(names))
print(names)

prices=[]
for i in soup.find_all(class_="a-price-whole"):
    prices.append(i.text)
print(len(prices))
print(prices)

urls = []
links = []
for link in soup.find_all('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal", target="_blank"):
    urls.append(link.get("href"))

for l in urls:
    link = "https://www.amazon.in" + str(l)
    links.append(link)
print(links)


a = {'Name' : names , 'Price': prices , 'Link' : links }
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df.to_csv("data.csv")