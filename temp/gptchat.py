import csv
import pandas as pd

# Open the input CSV file
with open("input.csv", "r") as input_file:
    # Read the contents of the file into a pandas DataFrame
    df = pd.read_csv(input_file)

# Group the rows of the DataFrame by the start and end coordinates
grouped = df.groupby(["start_longitude", "start_latitude", "end_longitude", "end_latitude"])

# Create a list of unique coordinates
coords = grouped.apply(lambda x: x.iloc[0]).reset_index(drop=True)

# Create a DataFrame with columns for the ID, longitude, and latitude of each unique coordinate
coords_df = pd.DataFrame({"id": range(1, len(coords) + 1), "longitude": coords["start_longitude"], "latitude": coords["start_latitude"]})

# Write the DataFrame of coordinates to a CSV file
coords_df.to_csv("coordinates.csv", index=False)

# Add the IDs of the start and end coordinates to the rows of the original DataFrame
merged = pd.merge(df, coords_df, how="left", left_on=["start_longitude", "start_latitude"], right_on=["longitude", "latitude"])
merged = merged.rename(columns={"id": "start_id"})
merged = pd.merge(merged, coords_df, how="left", left_on=["end_longitude", "end_latitude"], right_on=["longitude", "latitude"])
merged = merged.rename(columns={"id": "end_id"})

# Create a DataFrame with columns for the date, ID of the start coordinate, ID of the end coordinate, and flow of the journey
journeys_df = pd.DataFrame({"date": merged["date"], "from_id": merged["start_id"], "to_id": merged["end_id"], "flow": merged["flow"]})

# Write the DataFrame of journeys to a CSV file
journeys_df.to_csv("journeys.csv", index=False)


'''
Here is a basic outline of a Python script that you can use to achieve your desired outcome:

Import the necessary libraries, such as csv for working with CSV files, and pandas for data manipulation.

Open the input CSV file using the csv.reader() function, and read the contents of the file into a pandas DataFrame.

Use the pandas groupby() function to group the rows of the DataFrame by the start and end coordinates of the journeys. This will allow you to create a list of unique coordinates.

Use the pandas drop_duplicates() function to remove any duplicate coordinates from the list.

Create a new DataFrame with columns for the ID, longitude, and latitude of each unique coordinate. Use the pandas reset_index() function to create a sequential ID for each coordinate.

Write the DataFrame to a CSV file using the pandas to_csv() function.

Use the pandas merge() function to combine the original DataFrame with the DataFrame of unique coordinates, using the start and end coordinates as the key. This will add the ID of the start and end coordinates to the rows of the original DataFrame.

Create a new DataFrame with columns for the date, ID of the start coordinate, ID of the end coordinate, and flow of the journey.

Write the DataFrame to a CSV file using the pandas to_csv() function.

You can adapt this script to fit your specific needs, and add any additional processing or data manipulation steps as needed.


Request: i have a .csv file with the columns "date","start_longitude", start_latitude", "end_longitude", "end_latitude", "flow". The columns with coordinates specify a journey from point a to point b. The flow column specifies the amount of travel between these points. I want to write a python script that takes a file like this as an input, and spits out two .csv files: One with unique locations, with an ID assigned to each, so columns are: "id", "longitude", "latitude". The other file then contains the pairs of locations that represents the journeys taken. So columns here are: "date","from_id", "to_id","flow".
'''