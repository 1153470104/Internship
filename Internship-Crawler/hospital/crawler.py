"""
this program is aim to
store the specific info into the hos_dict
"""

import requests
import re
from bs4 import BeautifulSoup
import hospital.input_manager


def add(url, hos_dict, hos_number, child_number):
    str_html = requests.get(url)
    # print(str_html)
    soup = BeautifulSoup(str_html.text, 'lxml')

    """get the basic info"""
    data_level = soup.select(
        'body > div.wrapper > div.wrap-box > div.yy-cont > dl:nth-child(' + str(child_number) + ') > dd > b > samp')
    data_sort = soup.select(
        'body > div.wrapper > div.wrap-box > div.yy-cont > dl:nth-child(' + str(child_number) + ') > dd > b > span')
    data_address = soup.select(
        'body > div.wrapper > div.wrap-box > div.yy-cont > dl:nth-child(' + str(child_number) + ') > dd > p:nth-child(3)')
    data_level = trans_str(data_level)
    data_sort = trans_str(data_sort)
    data_address = trans_str(data_address)

    data_level = re.findall(r"samp>(.+?)</samp", data_level)[0]
    data_sort = re.findall(r"span>(.+?)</span>", data_sort)[0]
    data_address = re.findall(r"/span>(.+?)</p", data_address)[0]

    print(data_level)
    print(data_sort)
    print(data_address)

    # """add the info into the dict"""
    hos_dict[hos_number]['level'] = data_level
    hos_dict[hos_number]['sort'] = data_sort
    hos_dict[hos_number]['address'] = data_address


def trans_str(data):
    content_str = ''
    for x in data:
        content_str = content_str + str(x)
    return content_str


# add("https://so.99.com.cn/search.php?q=%E5%8C%BB%E9%99%A2&m=&f=_all&s=relevance&p=1&proj=yyk", 0, 0, 1)
