# coding=utf-8
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


html = getHtml("http://bj.lianjia.com/ershoufang/pg2/")

print html