from re import L
import urllib.request as req
from bs4 import BeautifulSoup
import csv
import codecs

#因為網站會有反爬蟲的設定，所以header的資訊是為了模擬使用者進入網站
#User-Agent為用戶端資訊
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"}
#url是要爬蟲的網站的網址
url="https://www.binance.com/zh-TW/markets"
res = req.urlopen(url)
content = res.read().decode("utf-8")


file = codecs.open("data.csv","w","utf-8")  #讀寫模式  w-新建檔案寫入 b-二進位模式
file.write(u'\ufeff')  #防止亂碼
writer = csv.writer(file)
writer.writerows(['幣種','價格','24h漲跌','24h成交量','市值'])
# lists = ['幣種','價格','24h漲跌','24h成交量','市值']
lists = []
parsedata=BeautifulSoup(content,"html.parser")#使用beautifulsoup解析HTML格式
for i in range (30):
    name = parsedata.select('div.css-1ap5wc6')[i].text
    price = parsedata.select('div.css-ydcgk2')[i].text
    updown = parsedata.select('div.css-1ca67uc')[i].text
    deal = parsedata.select('div.css-102bt5g')[i].text
    market_value = parsedata.select('div.css-s779xv')[i].text

    lists.append(name)
    lists.append(price)
    lists.append(updown)
    lists.append(deal)
    lists.append(market_value)
print(type(lists))
# writer.writerows(lists)

file.close()