import os
import pandas as pd

# get all the files in the directory with .csv extension
csv_files = [file for file in os.listdir("./csv_files") if file.endswith('.csv')]

# iterate over the csv files
# for csv_file in csv_files:
#     file = pd.read_csv('./csv_files/' + csv_file)
#     # print columns names
#     print("****************************************")
#     print('File: ' + csv_file)
#     print(file.columns)
#     print("****************************************")

# merge all csv files into one
# create an empty dataframe
df = pd.DataFrame()
for csv_file in csv_files:
    file = pd.read_csv('./csv_files/' + csv_file)
    df = df._append(file, ignore_index=True)
    print('File: ' + csv_file + ' appended to dataframe')
    
# save the dataframe as csv
df.to_csv('./csv_files/all_institutes.csv', encoding='utf-8', index=False)