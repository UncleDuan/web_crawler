import re
from lxml import etree
import requests

def download_video(url,name):
    response= requests.get(url)
    # 去除名字里的引号
    name=re.sub("[‘’“”\"']","",name)
    print(name)
    with open(name+'.mp4', "ab+") as f:
        f.write(response.content)
def get_video(url):
    response= requests.get(url)
    html = response.text
    link = re.findall('srcUrl="(.*?)"',html)
    print(link)
    name=re.findall('<title>(.*?)</title>',html)
    print(name)
    # 去除直播链接
    list=re.findall("直播：",name)
    if len(list)==0:
        download_video(link[0],name[0])
def LiIndex(url):
    response=requests.get(url)
    html=response.text
    html_xpath = etree.HTML(html)
    # Xpath提取url
    urls=html_xpath.xpath('//li/div/a/@href')
    print(urls)
    for liurl in urls:
        get_video(base_url+liurl)

base_url = "http://www.pearvideo.com/"
#梨视频中的“国际”分类
url=base_url+"category_2"
LiIndex(url)