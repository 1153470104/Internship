# -*- coding: UTF-8 -*-
import os
import pandas as pd

""" make a name list of the txt """
txt_path = "C:/Users/ThinkPad/Desktop/Internship/changeName/nameFormat.txt"
f = open(txt_path, "r", encoding='UTF-8')
name_list = []
for line in f:
    line = line[:-1]
    if "年份的" in line:
        name_list.append(line.split("年份的")[1])
    elif "年份、11" in line:
        name_list.append(line.split("年份、11")[1])
    elif "年份、22" in line:
        name_list.append(line.split("年份、22")[1])
    elif "年份、33" in line:
        name_list.append(line.split("年份、33")[1])
    elif "年份、44" in line:
        name_list.append(line.split("年份、44")[1])
    elif "年份、55" in line:
        name_list.append(line.split("年份、55")[1])
    elif "年份、66" in line:
        name_list.append(line.split("年份、66")[1])
    elif "年份、77" in line:
        name_list.append(line.split("年份、77")[1])
    elif "年份、" in line:
        name_list.append(line.split("年份、")[1])
    elif "年份" in line:
        name_list.append(line.split("年份")[1])

f.close()

for x in name_list:
    print(x)

csv_path = "C:/Users/ThinkPad/Desktop/Internship/out_csv"
out_csv_path = "C:/Users/ThinkPad/Desktop/Internship/output_csv"


def change_name(file_path, year, count):
    """ the change name method """
    os.rename(file_path, out_csv_path + "/" + year + "/"
              + "区县" + name_list[count - 1] + year + ".csv")


# excel_path = r"C:/Users/ThinkPad/Desktop/Internship/out_excel"

g = os.walk(csv_path)

""" iterate to change the file name and output to another folder"""
for path, dir_list, file_list in g:
    for file_name in file_list:
        count_str = file_name.split('_')[1]
        count = 0
        if len(count_str) < 4:
            count = int(count_str)
        else:
            count = int(count_str[0:-4])
        year = file_name[0:4]
        print("count: " + str(count))
        if len(file_name) > 11:
            0
        elif os.path.exists(out_csv_path + "/" + year):
            change_name(os.path.join(path, file_name), year, count)
        else:
            os.mkdir(out_csv_path + "/" + year)
            change_name(os.path.join(path, file_name), year, count)

    # for dir_name in dir_list:
    #     print(os.path.join(path, dir_name))
