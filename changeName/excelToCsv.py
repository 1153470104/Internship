import pandas as pd
import os


def xls_to_csv_pd(xls_path, csv_path):
    data_xls = pd.read_excel(xls_path, index_col=0)
    data_xls.to_csv(csv_path, encoding='utf-8')


excel_path = r"C:/Users/ThinkPad/Desktop/Internship/out_excel"
csv_path = "C:/Users/ThinkPad/Desktop/Internship/out_csv"

g = os.walk(excel_path)

for path, dir_list, file_list in g:
    for file_name in file_list:
        # print(os.path.join(path, file_name))
        # print(file_name)
        year = file_name[0:4]
        if os.path.exists(csv_path + "/" + year):
            out_xls = csv_path + "/" + year + "/" + file_name[0:-4] + ".csv"
            print(out_xls)
            # Execute ExcelToCsv
            xls_to_csv_pd(os.path.join(path, file_name), out_xls)
        else:
            os.mkdir(csv_path + "/" + year)
            out_xls = csv_path + "/" + year + "/" + file_name[0:-4] + ".csv"
            print(out_xls)
            # Execute ExcelToCsv
            xls_to_csv_pd(os.path.join(path, file_name), out_xls)

    # for dir_name in dir_list:
    #     print(os.path.join(path, dir_name))
