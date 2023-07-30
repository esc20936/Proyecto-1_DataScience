# python script to convert all .xls to .csv in a directory
import pandas as pd
import os

# get all the files in the directory
files = os.listdir("./xlsx_files")

# get all the files with .xls extension
xls_files = [file for file in files if file.endswith('.xlsx')]


# iterate over the xls files
for xls_file in xls_files:
    print('File: ' + xls_file)
    data_xls = pd.read_excel('./xlsx_files/' + xls_file,engine='openpyxl', index_col=None)
    data_xls.to_csv('./csv_files/' + xls_file[:-4] + '.csv', encoding='utf-8', index=False)
    print('File: ' + xls_file + ' converted to csv')
# Path: main.py