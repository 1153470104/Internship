"""
the aim of this program
is to match the hospital-name with the hospital-url
and store it into the dict list
"""
import requests
import re
from bs4 import BeautifulSoup
import hospital.input_manager
from hospital import crawler
import xlsxwriter

# get the dict & list of hospital
hos_dict = hospital.input_manager.input_dict()
hos_list = hospital.input_manager.name_list()

# first get the url definition
# 医院 url
url_yy1 = 'https://so.99.com.cn/search.php?q=%E5%8C%BB%E9%99%A2&m=&f=_all&s=relevance&p='
url_yy2 = '&proj=yyk'
path_yy1 = 'body > div.wrapper > div.wrap-box > div.yy-cont > dl:nth-child('
path_yy2 = ') > dd > b > a'

# 保健院
url_bjy1 = ''
url_bjy2 = ''


def hos_page_content(page_url, selector):
    """use url selector to get page content"""
    str_html = requests.get(page_url)
    soup = BeautifulSoup(str_html.text, 'lxml')

    hos_content = soup.select(selector)
    # print(hos_content)
    content_str = ''
    for x in hos_content:
        content_str = content_str + str(x)
    print(content_str)
    return content_str


def page_match(raw_info):
    """
    input with raw info contains the hos-name & page url
    manipulate the dict of hospital information
    """
    hos_url = re.findall(r"href=\"(.+?)\"", raw_info)[0]
    hos_name = re.findall(r"title=\"(.+?)\"", raw_info)[0]
    hos_number = name_exist(hos_name)
    print(hos_number)
    if hos_number > -1:
        # crawler.add(hos_dict, hos_number, hos_url)
        return hos_number
    return -1


def name_exist(name):
    i = 0
    for x in hos_dict:
        if x['name'] == name:
            return i
        i = i + 1
    return -1


def article_iterate(page_url, path_part1, path_part2):
    """iterate & dealing all 10 the potential hos on one page"""
    # there may be some page with article quantity less than 10
    # if there's no content the method just return an empty list
    # so I choose to add a simple judge
    for i in range(10):
        k = i + 1
        article_content = hos_page_content(page_url, path_part1 + str(k) + path_part2)
        if article_content:
            number = page_match(article_content)
            if number > -1:
                crawler.add(page_url, hos_dict, number, k)


def page_iterate(url_part1, url_part2):
    """iterate all page of the search of specific keywords of hos"""
    # there may be some fake url
    # since a page with out any content could be request as usual
    # I just use for loop

    # the true number is 2645
    for i in range(46):
        k = i+2600
        print(k)
        article_iterate(url_part1 + str(k) + url_part2, path_yy1, path_yy2)
        if k % 100 == 0:
            save_excel(hos_dict)
    print('\nfinish!!!')


def fill_ratio():
    """calculate the filled ratio of hos-dict"""
    i = 0.0
    for x in hos_dict:
        if 'level' in x:
            i = i+1
    print('filled ' + str(i) + ' entries')
    return i/len(hos_dict)


def print_list(hos_dictionary):
    for a in hos_dictionary:
        print(a)


def save_excel(dictionary):
    workbook = xlsxwriter.Workbook('dict1.xlsx')
    worksheet = workbook.add_worksheet('医院')
    row = 0
    col = 0

    # 按照行和列写入数据
    for x in dictionary:
        worksheet.write(row, col, x['name'])
        if 'level' in x:
            worksheet.write(row, col + 1, x['level'])
            worksheet.write(row, col + 2, x['sort'])
            worksheet.write(row, col + 3, x['address'])

        row += 1

    # 关闭并保存表格内容
    workbook.close()


"""main test function"""
page_iterate(url_yy1, url_yy2)
print_list(hos_dict)
print(fill_ratio())

"""test excel save"""
save_excel(hos_dict)

"""some early test part"""
# url = url_yy1 + '1' + url_yy2
# path = 'body > div.wrapper > div.wrap-box > div.yy-cont > dl:nth-child(1) > dd > b > a'
# content = hos_page_content(url, path)
# print(content)
# print(type(content))
# print(re.findall(r"href=\"(.+?)\"", content))
# print(re.findall(r"href", content))

"""to test debug the str equals problem"""
# case_url = 'https://so.99.com.cn/search.php?q=%E5%8C%BB%E9%99%A2&m=&f=_all&s=relevance&p=1&proj=yyk'
# raw_info = hos_page_content(case_url, path_yy1 + '1' + path_yy2)
# hos_url = re.findall(r"href=\"(.+?)\"", raw_info)[0]
# hos_name = re.findall(r"title=\"(.+?)\"", raw_info)[0]
# case_name = '昆山中医院东方医院合作医院'
# print(type(hos_name))
# print(hos_name == case_name)
