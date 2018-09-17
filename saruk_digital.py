import requests
from lxml import html
import pandas as pd
import time
s = time.time()
headers = '	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
url = 'https://saruk.co.ke/products/category/laptops'

page=requests.get(url)
tree = html.fromstring(page.content)
details = []
for i in range(1,101):
	name = tree.xpath('//*[@id="grid-extended"]/ul/li['+str(i)+']/div/div/a/h3/text()')
	price_now = tree.xpath('//*[@id="grid-extended"]/ul/li['+str(i)+']/div/div/div/span/span/ins/span/text()')
	price_before = tree.xpath('//*[@id="grid-extended"]/ul/li['+str(i)+']/div/div/div/span/span/del/span/text()')
	details.append((str(name).strip("'[]'"),str(price_now).strip("'[]'"),str(price_before).strip("'[]'")))

df = pd.DataFrame(details, columns=['Name','Price Now','Price Before'])
print(df)
f = time.time()
print("T took:",str(f - s))
