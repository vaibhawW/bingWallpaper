from BeautifulSoup import BeautifulSoup as bs
from requests import get
from urllib import urlretrieve as urlR
import os

#getting the url
bing=get('http://www.bing.com').text

#extracting the image url and compiling it
index=bing.find('.jpg')
partUrl=bing[index-100:index+4]
imageLink="http://www.bing.com"+partUrl.split('url: "')[1]

#downloading the image link
urlR(imageLink,"bing.jpg")

#setting image
os.system("gsettings set org.gnome.desktop.background picture-uri file://"+os.getcwd()+"/bing.jpg")
