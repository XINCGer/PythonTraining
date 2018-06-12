#coding:utf-8
import urllib2
import urllib

# 简单使用urllib
#response = urllib2.urlopen("https://cuiqingcai.com/947.html")
#print response.read()

# 构造Request
# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()

# post模拟登录
# values = {"username":"1016903103@qq.com","password":"XXXX"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()

# get模拟登录
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl