# -*- coding: utf-8 -*-

import urllib2
import re
#import sms
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='log.log'
                    )


def del_html_mark(content):
    inner_pattern = re.compile('<.*?>')
    return re.sub(inner_pattern, '', content)


def del_additional_mark(content):
    inner_pattern = re.compile('&nbsp')
    content = re.sub(inner_pattern, '', content)
    inner_pattern = re.compile('[;\t\n ]')
    content = re.sub(inner_pattern, '', content)
    return content


def handle_content(content):
    content = del_html_mark(content)
    content = del_additional_mark(content)
    return content


url = 'http://hz.5i5j.com/exchange/_%E4%B9%8B%E6%B1%9F%E4%B8%80%E5%8F%B7'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Waoindows NT)'
headers = {'User-Agent': user_agent}
html_content = ''
logging.info('Starting scanning...')
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html_content = response.read()
    # print html_content
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

content = html_content.decode('utf-8')
pattern = re.compile('<div class="list-info">(.*?)</div>', re.S)
items = re.findall(pattern, content)
for item in items:
    title_pattern = re.compile('<h2><a href=.*?>(.*?)</a></h2>')
    title_list = re.findall(title_pattern, item)
    title = title_list[0]
    title = handle_content(title)
    # print title
    community_pattern = re.compile('<a href=.*? target="_blank"><h3 >(.*?)</h3></a>')
    community_list = re.findall(community_pattern, item)
    community = community_list[0]
    community = handle_content(community)
    # print community
    detail_pattern = re.compile('<li class="font-balck">(.*?)</li>')
    detail_list = re.findall(detail_pattern, item)
    detail = detail_list[0]
    detail = handle_content(detail)
    # print detail
    price_pattern = re.compile('<h3>(.*?)</em></h3>')
    price_list = re.findall(price_pattern, item)
    price = price_list[0]
    price = handle_content(price)
    # print price
    size_pattern = re.compile('<p>(.*?)/.*?</p>')
    size_list = re.findall(size_pattern, item)
    size = size_list[0]
    size = handle_content(size)
    total_msg = {
        'title': title.encode('utf-8'),
        'community': community.encode('utf-8'),
        'detail': detail.encode('utf-8'),
        'price': price.encode('utf-8'),
        'size': size.encode('utf-8')
    }
    file = open('record.log', 'r')
    old_info_list = file.readlines()
    for old_info in old_info_list:
        old_info = del_additional_mark(old_info)
    file.close()
    is_old_message = False
    for old_info in old_info_list:
        if old_info == (total_msg['title'] + '\n'):
            is_old_message = True
            break
    if is_old_message:
        continue
    file = open('record.log', 'a')
    print total_msg
    #sms.send_msg(total_msg, '我的手机号码')
    file.write(total_msg['title'] + '\n')
    file.close()
logging.info(total_msg['title'])
logging.info(total_msg['detail'])
logging.info(total_msg['community'])
logging.info(total_msg['size'])
logging.info(total_msg['price'])
logging.info('Finished scanning.')
file.close()