#感谢 blueberryc 的分享
# web_crawler
爬虫的相关笔记和代码<br /> 
相关教程在https://zhuanlan.zhihu.com/p/42078956#__NO_LINK_PROXY__<br /> 
试了一下里面的爬网易云音乐的模块<br /> 

主要是：<br /> 
* 1.pip install selenium<br /> 
  并安装webdriver，提供了四个浏览器的，https://selenium-python.readthedocs.io/installation.html#drivers<br /> 
  这里面有一个selenium的小范例程序：<br /> 
  ```python
          from selenium import webdriver
          driver = webdriver.Chrome()
          driver.get('https://www.baidu.com')
          print(driver.title)
          driver.quit()
  ```
  对于像我这种没用过selenium的很友善。<br /> 
  安装谷歌浏览器的ChromeDriver可能要翻墙<br /> 
* 2.pip install pandas<br /> 
  这个是用来处理csv文件的。<br /> <br /> 
  csv文件是文本文件，逗号分列，回车分行，用来描述表格数据。<br /> 
* 3.好像运行久了出了一个bug，没有爬完。<br /> 
* 4.用Excel直接打开.csv问价，歌名会出现乱码。<br /> 
