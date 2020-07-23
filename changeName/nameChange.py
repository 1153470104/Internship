import os
import pandas as pd


# 合并所有文件
def joint_csv(folder_path, saveFile_path, saveFile_name, amount):

# excel_path = r"C:/Users/ThinkPad/Desktop/Internship/out_excel"
csv_path = "C:/Users/ThinkPad/Desktop/Internship/out_csv"

g = os.walk(csv_path)

for path, dir_list, file_list in g:
    # pre_name = ''
    # count = 0
    # for file_name in file_list:
    #     if file_name[0:6] == pre_name:
    #         count = count + 1
    #     else:
    #         if count != 0:
    #             joint_csv(csv_path + "/" + pre_name[0:4]
    #                       , csv_path + "/" + pre_name[0:4], pre_name, count)
    #         pre_name = file_name[0:6]
    #         count = 0

        # print(os.path.join(path, file_name))
        # print(file_name)

    # for dir_name in dir_list:
    #     print(os.path.join(path, dir_name))
