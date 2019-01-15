#coding:utf8
from  urllib import request
# resp = request.urlopen('https://www.baidu.com') #crtl + b 看函数功能
# print(resp.readline())
# print(resp.readlines())
# print(resp.getcode())

#下面函数的用法
# request.urlretrieve('http://upload.gezila.com/data/20161013/86451476325005.jpg','wangzhe.jpg') #下载到本地
from urllib import parse
# params = {'name':'张三' , "age":18 ,'greet':'hello world'}
# result = parse.urlencode(params)
# print(result)


#函数的用法
# url= 'https://www.baidu.com/s?wd=刘德华'
# url= 'https://www.baidu.com/s'
# params = {"wd":"刘德华"}
# qs = parse.urlencode(params)
# # print(qs)
# url = url+"?"+qs
# # print(url)
# resp = request.urlopen(url)
# print(resp.read())

#parse_qs函数的用法 解码
# params = {'name':'张三' , "age":18 ,'greet':'hello world'}
# qs = parse.urlencode(params)
# print(qs)
# result = parse.parse_qs(qs)
# print(result)

