# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import tool
import os


# 获取MM个人详情页面
def getDetailPage(infoURL):
    response = urllib2.urlopen(infoURL)
    return response.read().decode('gbk')


# 获取个人文字简介
def getBrief(page):
    pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
    result = re.search(pattern, page)
    return tool.replace(result.group(1))


# 获取页面所有图片
def getAllImg(page):
    pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
    # 个人信息页面所有代码
    content = re.search(pattern, page)
    # 从代码中提取图片
    patternImg = re.compile('<img.*?src="(.*?)"', re.S)
    images = re.findall(patternImg, content.group(1))
    return images

if __name__ == '__main__':
    #print ("------begin--------")
    url = 'http://mm.taobao.com/91442126.htm'
    print "url=", url

    detailPage = getDetailPage(url)
    print "detailPage=", detailPage

    # 获取个人简介
    brief = getBrief(detailPage)
    print "brief=", brief

    # 获取所有图片列表
    images = getAllImg(detailPage)
    print "images=", images

    # self.mkdir(item[2])
    # 保存个人简介
    # self.saveBrief(brief, item[2])
    # 保存头像
    # self.saveIcon(item[1], item[2])
    # 保存图片
    # self.saveImgs(images, item[2])

    #print ("------end--------")
