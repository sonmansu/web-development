import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# print(trs)

music = soup.select_one('#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number')
# print(music.text)
num = music.text.split(' ')[0].strip()
# num = music.text.strip()
# print(num)

for tr in trs:
    rank = tr.select_one('td.number').text.split(' ')[0].strip()
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    singer = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, singer)
    # print(singer)
