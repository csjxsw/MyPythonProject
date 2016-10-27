# coding=utf-8
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)  # 打开
    html = page.read()  # 读取
    return html


def getimg(html):
    reg = r'src="(.+\.jpg)"'  # 正则进行匹配，‘.’是通配符，\是转意
    print reg  # 只是输出来看看是否有大的错误
    imgre = re.compile(reg)  # 开始正则的匹配。
    imglist = re.findall(imgre, html)  # 获取图片链表
    print imglist  # 输出这个列表
    x = 0  # 标号
    for imgurl in imglist:  # 遍历这个列表
        urllib.urlretrieve(imgurl, '%s.jpg' % x)  # 把列表中的每一个都保存下来，取名为 x.jpg
        x += 1


html = getHtml('http://tieba.baidu.com/p/4133040044')
print (getimg(html))