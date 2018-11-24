## 爬取糗百并保存
[Beautifulsoup4 find_all函数](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all)
### find_all( name , attrs , recursive , text , **kwargs )
* name 参数
    name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉.
* keyword 参数
    如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性.
* 按CSS搜索
    按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag
### get_text()
    如果只想得到tag中包含的文本内容,那么可以嗲用 get_text() 方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回
