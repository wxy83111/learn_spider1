# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:34:47 2016

@author: WilliamWoo
"""
import urllib.request
from http.cookiejar import CookieJar
#装入相关模块

url = 'http://www.baidu.com'    #定义待爬取网址


cookie = CookieJar()
#获取Cookiejar对象（存在本机的cookie消息）
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
#自定义opener,并将opener跟CookieJar对象绑定
urllib.request.install_opener(opener)
#安装opener,此后调用urlopen()时都会使用安装过的opener对象


fakeheader = urllib.request.Request(url)
fakeheader.add_header('user-agent','Mozilla/5.0\
 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
#把Key和Value写入对象（实例），修改HTTP中的header，伪装成浏览器（其中\为续行符）

response1 = urllib.request.urlopen(fakeheader)
pagehtml1 = response1.read()        #读取网页内容
print (response1.getcode())
print('status',response1.status, response1.reason)
#查询网页读入状态码200为成功，404为未找到,以上两者功能类似。

for k,v in response1.getheaders():
    print('%s: %s' % (k,v))
    #读取HTTP响应头与JSON数据
print (len(pagehtml1))    #显示网页长度
print (cookie)    #打印cookie数据
    
if __name__ == '__main__':
 #仅在系统控制台中运行时显示下列内容 
    print('end')
  

