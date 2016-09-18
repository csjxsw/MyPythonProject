import urllib2 as url

response = url.urlopen('http://www.baidu.com/')
html = response.read()
print html
