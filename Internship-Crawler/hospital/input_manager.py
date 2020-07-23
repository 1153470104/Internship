"""
transform excel data into structural data
use for hospital name match & excel output
"""

import xlrd
import re


def get_name():
    """get the data of excel sheet"""
    data = xlrd.open_workbook('hospital_sheet.xls')
    table = data.sheets()[0]
    # print(table)
    hospital_name = table.col_values(1)
    return hospital_name
    # print(hospital_name)


def reformat(hos_name):
    """reformat the name of hospitals"""
    hos_name.pop(0)  # with a delete occurs error
    # b = "北京市肛肠医院（北京市西城区二龙路医院)"
    # b = re.sub(u"（.*?\\)", "", b)
    # print(b)

    # an ugly realization, but with so ugly input, wish there's a better solution
    i = 0
    for a in hos_name:
        hos_name[i] = re.sub(u"（.*?\\)", "", a)
        hos_name[i] = re.sub(u"\\(.*?\\)", "", hos_name[i])
        hos_name[i] = re.sub(u"（.*?）", "", hos_name[i])
        hos_name[i] = re.sub(u"\\(.*?）", "", hos_name[i])

        head, sep, tail = hos_name[i].partition('、')
        hos_name[i] = head

        i = i + 1


def name_list():
    return reformat(get_name())


def make_dict(hos_name):
    """ make a new data structure"""
    hos_data = list()
    for a in hos_name:
        hos_data.append({'name': a})
    return hos_data


# the final step is to encapsulate this into a method
def input_dict():
    """main function"""
    name = get_name()
    reformat(name)
    # print(name)
    data = make_dict(name)
    # print(data)
    # data[0]['level'] = '三级甲等'
    # print_list(data)
    return data


def print_list(list):
    for a in list:
        print(a)


# input_dict()
