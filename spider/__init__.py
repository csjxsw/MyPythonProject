import urllib2 as url

req = url.Request("http://www.baidu.com")

try:
    response = url.urlopen(req)
    page = response.read()
    print (page)
except url.URLError, e:
    print e.reason
else:
    print 'No exception was raised.'
