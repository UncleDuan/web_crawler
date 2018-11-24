import re
from lxml import etree
import requests
base_url = "http://www.pearvideo.com/"
url=base_url+"category_2"

def download_video(url,name):
    response= requests.get(url)
    with open(name+'.mp4', "ab+") as f:
        f.write(response.content)
def get_video(url):
    response= requests.get(url)
    html = response.text
    link = re.findall('srcUrl=".*?"',html)
    print(link)
    name=re.findall('<title>(.*?)</title>',html)
    print(name)
    download_video(url,name[0])
def LiIndex(url):
    response=requests.get(url)
    html=response.text
    html_xpath = etree.HTML(html)
    urls=html_xpath.xpath('//li/div/a/@href')
    print(urls)
    for liurl in urls:
        get_video(base_url+liurl)


LiIndex(url)