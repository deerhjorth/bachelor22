# This script combines SI and daily flow data into data suited for Flourish
# Takes our data as input, spits a .csv file

import pandas as pd

def data_transform(si_data_path,flow_data_path,combined_data_filename):
    combined_data_filename = str(combined_data_filename)
    si_data = pd.read_csv(si_data_path)
    si_data = si_data[['Date_index', 'StringencyIndex']]
    si_data.columns = ['date', 'stringency_index']
    si_data = si_data[si_data["date"].str.contains('2020')]
    flow_data = pd.read_csv(flow_data_path)
    flow_data = flow_data[flow_data["date"].str.contains('2020')]
    combined_data = pd.merge(si_data, flow_data,how = 'inner', on = 'date')
    # rolling avg below
    combined_data['rolling_avg'] = combined_data.rolling(window=7)['flow_nonlog'].mean()
    combined_data.to_csv(combined_data_filename, index=False)

si_data_path = str(input("Enter absolute path to SI data: "))
flow_data_path = str(input("Enter absolute path to flow data: "))

save_to_current_dir = str(input("Do you want to save the transformed data to the current directory? (y/n): ")).lower().strip()
if save_to_current_dir == 'y':
    combined_data_filename = str(input("Enter filename (.csv) for combined SI/mobility file: "))
elif save_to_current_dir == 'n':
    combined_data_filename = str(input("Enter absolute path with filename (.csv) for combined SI/mobility file: "))

data_transform(si_data_path, flow_data_path, combined_data_filename)