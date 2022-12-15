# This script limits a lines.csv data set for a specific city to a certain date range
# Takes e.g. bog_lines.csv data as input, spits out a .csv file

import pandas as pd

def limit_dates(input_file_path, date_from, date_to, limited_data_filename):
    lines_data = pd.read_csv(input_file_path)
    limited_lines_data = lines_data[(lines_data['date'] >= date_from) & (lines_data['date'] < date_to)]
    limited_lines_data.to_csv(limited_data_filename, index=False)

input_file_path = str(input("Enter absolute path to lines data: "))
date_from = str(input("Enter start date (format: yyyy-mm-dd): "))
date_to = str(input("Enter end date (this date won't be included) (format: yyyy-mm-dd): "))
save_to_current_dir = str(input("Do you want to save the transformed data to the current directory? (y/n): ")).lower().strip()
if save_to_current_dir == 'y':
    limited_data_filename = str(input("Enter filename (.csv) for date limited lines file: "))
elif save_to_current_dir == 'n':
    limited_data_filename = str(input("Enter absolute path with filename (.csv) for date limited lines file: "))

limit_dates(input_file_path, date_from, date_to, limited_data_filename)