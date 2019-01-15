#coding:utf8
from urllib import  parse
url = 'http://www.baidu.com/s?wd-python&username-abc#1'
result1 = parse.urlsplit(url)
result2 = parse.urlparse(url)
print(result1)
print(result2)

# print('scheme:',result.scheme)
# print('netloc:',result.netloc)
# print('path:',result.path)
# # print('params:',result.params)
# print('query:',result.query)
# print('fragment:',result.fragment)
#urlsplit 没有params这个 而且这个用的很少 完全可以忽略掉

#urlopen 没有请求头



