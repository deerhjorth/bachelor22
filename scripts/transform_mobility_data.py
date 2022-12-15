# This script transforms mobility data to fit Flourish format
# Takes our data as input, spits out two .csv files for Flourish

import pandas as pd

def data_transformation(path,locations_filename,lines_filename):
    
    locations_filename = str(locations_filename)
    lines_filename = str(lines_filename)
    mobility_data = pd.read_csv(path)
    locations = pd.DataFrame(columns=["LocID", "lon", "lat"])
    lines = pd.DataFrame(columns=["date","sourceID", "targetID","flow"])
    id_list = list(range(0,2000000))
    for i in mobility_data.values:
        date = i[0]
        flow = i[5]
        loc_df_len = len(locations)
        lines_df_len = len(lines)

        if not ((locations.lon == i[1]) & (locations.lat == i[2])).any():
            id_to_use = id_list[0]
            to_append = [id_to_use, i[1], i[2]]
            locations.loc[loc_df_len] = to_append
            id_list.pop(0)
        else:  
            id_to_use = locations.loc[(locations.lon == i[1]) & (locations.lat == i[2]), 'LocID'].iloc[0]

        from_id = id_to_use

        if not ((locations.lon == i[3]) & (locations.lat == i[4])).any():
            id_to_use = id_list[0]
            to_append = [id_to_use, i[3], i[4]]
            locations.loc[loc_df_len+1] = to_append
            id_list.pop(0)
        else:
            id_to_use = locations.loc[(locations.lon == i[3]) & (locations.lat == i[4]), 'LocID'].iloc[0]

        to_id = id_to_use
        lines_append = [date,from_id,to_id,flow]
        lines.loc[lines_df_len] = lines_append
        

    locations['LocID'] = locations['LocID'].astype('int')
    lines[['sourceID','targetID']] = lines[['sourceID','targetID']].astype('int')

    # locations.to_csv('transformed_data/{}'.format(locations_filename), index=False)
    # lines.to_csv('transformed_data/{}'.format(lines_filename), index=False)
    locations.to_csv((locations_filename), index=False)
    lines.to_csv((lines_filename), index=False)

path = input("Enter aboslute path to mobility file: ")

# Desired path of locations and lines files
save_to_current_dir = str(input("Do you want to save the transformed data to the current directory? (y/n): ")).lower().strip()
if save_to_current_dir == 'y':
    locations_filename = str(input("Enter filename (.csv) for locations file: "))
    lines_filename = str(input("Enter filename (.csv) for lines file: "))
elif save_to_current_dir == 'n':
    locations_filename = str(input("Enter absolute path with filename (.csv) for locations file: "))
    lines_filename = str(input("Enter absolute path with filename (.csv) for lines file: "))


data_transformation(path, locations_filename, lines_filename)