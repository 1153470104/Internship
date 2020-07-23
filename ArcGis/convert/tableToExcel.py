import arcpy
import os

# workspace = "C:/Users/ThinkPad/Desktop/Internship/table_set.gdb"
#
# walk = arcpy.da.Walk(workspace, datatype="FeatureClass", type="Polygon")
# for dirpath, dirnames, filenames in walk:
#     for filename in filenames:
#         print filename

arcpy.env.workspace = "C:/Users/ThinkPad/Desktop/Internship/table_set.gdb"
pre_out_path = "C:/Users/ThinkPad/Desktop/Internship/out_excel"
tables = arcpy.ListFiles()
print tables
for filename in tables:
    if filename[0:2] == "qx":
        year = filename[2:6]
        if os.path.exists(pre_out_path + "/" + year):
            out_xls = pre_out_path + "/" + year + "/" + filename[2:] + ".xls"
            print out_xls
            # Execute TableToExcel
            arcpy.TableToExcel_conversion(filename, out_xls)
        else:
            os.mkdir(pre_out_path + "/" + year)
            out_xls = pre_out_path + "/" + year + "/" + filename[2:] + ".xls"
            print out_xls
            # Execute TableToExcel
            arcpy.TableToExcel_conversion(filename, out_xls)
