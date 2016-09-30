import re
import os
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

def savaImgToLocal(imglist):
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, 'E:\\crawler\\%s.jpg' % x)
        x +=1

html = getHtml("http://tieba.baidu.com/p/2460150866")
imglist = getImg(html)
for pic in imglist:
    print pic
savaImgToLocal(imglist)
print "---------------end----------------"
