# ---------------------------------------------------------------------------
# tocsv.py
# Created on: 11/29/2017
# By: Michael A. Carson
# Description: Exports feature attributes or a table to a CSV file.
# Note: Make changes to the input_fct, output_csv, and csv_delimiter
#       variables for your data.
# ---------------------------------------------------------------------------

# Import modules

import arcpy
import csv

# Change these variable values for your data


input_fct = "C:/Users/ThinkPad/Desktop/Internship/table_set.gdb/"
output_csv = "C:/Users/ThinkPad/Desktop/Internship/direct_csv/"
csv_delimiter = ","


def convert_to_csv(input_table, csv_name):
    # Set overwrite output if the same name
    arcpy.env.overwriteOutput = True

    # Read in fields and get field names
    fld_list = arcpy.ListFields(input_table)
    fld_names = [fld.name for fld in fld_list]

    # Open the CSV file and write out field names and data
    with open(csv_name, 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter=csv_delimiter)
        writer.writerow(fld_names)
        with arcpy.da.SearchCursor(input_table, fld_names) as cursor:
            for row in cursor:
                writer.writerow(row)
        csv_file.close()


# convert_to_csv(input_fct + "qx2006_1", output_csv + "qx2006_1.csv")
