import os
import pandas as pd


# 合并所有文件
def joint_csv(folder_path, saveFile_path, saveFile_name, amount):
    # 修改当前工作目录
    os.chdir(folder_path)
    # 将该文件夹下的所有文件名存入一个列表
    same_file_list = [saveFile_name + ".csv"]
    for i in range(amount):
        same_file_list.append(saveFile_name + "_" + str(i+1) + ".csv")

    # 读取第一个CSV文件并包含表头
    df = pd.read_csv(folder_path + '\\' + same_file_list[0])  # 编码默认UTF-8

    # 将读取的第一个CSV文件写入合并后的文件保存
    df.to_csv(saveFile_path + '\\' + same_file_list[0], encoding="utf_8_sig", index=False)

    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
    for i in range(1, len(same_file_list)):
        df = pd.read_csv(folder_path + '\\' + same_file_list[i])
        df.to_csv(saveFile_path + '\\' + same_file_list[0]
                  , encoding="utf_8_sig", index=False, header=False, mode='a+')


# def get_pre_name(filename):
#     if len(filename) == 8:
#         return filename
#     elif len(filename) == 10:
#         return filename[0:8]
#     else:
#         return filename[0:7]

def get_pre_name(filename):
    if len(filename) == 11:
        return filename[0:7]
    elif len(filename) == 13:
        return filename[0:7]
    else:
        return filename[0:6]

# excel_path = r"C:/Users/ThinkPad/Desktop/Internship/out_excel"
csv_path = "C:/Users/ThinkPad/Desktop/Internship/out_csv"

g = os.walk(csv_path)

for path, dir_list, file_list in g:
    pre_name = ''
    count = 0
    for file_name in file_list:
        print(pre_name)
        print(count)
        print(file_name)
        if get_pre_name(file_name) == pre_name:
            count = count + 1
        else:
            if count != 0:
                joint_csv(csv_path + "/" + pre_name[0:4]
                          , csv_path + "/" + pre_name[0:4], pre_name, count)
            pre_name = get_pre_name(file_name)
            count = 0
        # print(os.path.join(path, file_name))
        # print(file_name)

    # for dir_name in dir_list:
    #     print(os.path.join(path, dir_name))
