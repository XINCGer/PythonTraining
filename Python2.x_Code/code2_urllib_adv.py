#coding:utf-8

import urllib2
import urllib

# 设置header agent
# url = 'http://www.server.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username' : 'cqc',  'password' : 'XXXX' }
# headers = { 'User-Agent' : user_agent ,'Referer':'http://www.zhihu.com/articles'}
# data = urllib.urlencode(values)
# request = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(request)
# page = response.read()

# headers属性
# User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
# Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
# application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
# application/json ： 在 JSON RPC 调用时使用
# application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
# 在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务

# 代理使用Proxy
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)

# timeout 设置
# response = urllib2.urlopen('http://www.baidu.com', timeout=10)
# response = urllib2.urlopen('http://www.baidu.com',data, 10)

# 使用HTTP的PUT或者DELETE

# request = urllib2.Request(uri, data=data)
# request.get_method = lambda: 'PUT' # or 'DELETE'
# response = urllib2.urlopen(request)

# 使用DebugLog
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')