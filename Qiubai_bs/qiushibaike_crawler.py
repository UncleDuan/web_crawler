'''
按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.
从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag
'''
#本实例用于获取糗事百科热门的文章内容和好评数量。
import csv

import pandas as pd
import urllib
import os
from bs4 import BeautifulSoup
#糗事百科需要设置MIME头才能正常请求，不需要登陆，也不需要cookie
print('=======================糗事百科数据挖掘==========================')

urlstr="https://www.qiushibaike.com/8hr/page/%d"

FILE_NAME='qiushibaike.csv'
data={}
list_info=[]
def getdata(html):  #从字符串中安装正则表达式获取值
    soup = BeautifulSoup(html, 'html.parser');
    alldiv = soup.find_all("div", class_="content")   #内容的外部div
    allnum = soup.find_all("span", class_="stats-vote")  #点赞数量的外部span
    for i in range(0,len(alldiv)):
        list_one = [allnum[i].find_all('i')[0].string, (str(alldiv[i].find_all('span')[0]).replace('<span>', '').replace('</span>', '').replace('<br/>', '\r\n').strip())] # 内容文字，使用string在文字里还有<br/>时，无法打印，使用text会省略调用<br/>
        list_info.append(list_one)






#根据一个网址，获取该网址中符合指定正则表达式的内容
def craw(url):
    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }  #设置MIME头，糗事百科对这个进行了验证
        request = urllib.request.Request(url,headers = headers)  #创建一个请求
        response = urllib.request.urlopen(request)  #获取响应
        html = response.read()  #读取返回html源码
        getdata(html)
    except urllib.error.URLError as e:
        if hasattr(e,"Zhihu"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

def file_do(list_info):
        # 获取文件大小

        file_size = os.path.getsize(FILE_NAME)
        if file_size == 0:
            # 表头
            name = ['点赞数量','评论']
            # 建立DataFrame对象
            file_test = pd.DataFrame(columns=name, data=list_info)
            # 数据写入
            file_test.to_csv(FILE_NAME, encoding='utf-8', index=False)
        else:
            with open(FILE_NAME, 'a+', newline='',encoding='utf-8') as file_test:
                # 追加到文件后面
                writer = csv.writer(file_test)
                # 写入文件
                writer.writerows(list_info)
for i in range(1,14):
    url = urlstr % i
    print(url)
    craw(url)
file_do(list_info)

# 原文：https://blog.csdn.net/luanpeng825485697/article/details/78403943