
import requests 
from bs4 import BeautifulSoup
import json

url = 'https://www.azlyrics.com/lyrics/shayneward/icry.html'
response = requests.get(url)
html_soup = BeautifulSoup(response.text , 'html.parser')
singer = html_soup.find('div' , class_ = 'lyricsh').h2.text
song_name = html_soup.find('div' , class_ = 'col-xs-12 col-lg-8 text-center').find_all('div',class_= 'div-share')[1].text.split('"')[1]
lyrics = html_soup.find('div' , class_ = 'col-xs-12 col-lg-8 text-center').find_all('div')[5].text

data = {}
data['singer'] = singer
data['song_name'] = song_name
data['lyrics'] = lyrics

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
