# data.py
# This script reads a CSV file and prints the mean and median of each numeric column.
# Author: Shamila
# Date: 07/05/2025


import pandas as pd # Import the pandas library
# Define the path to the CSV file
data = pd.read_csv('data.csv')
for column in data.columns: # Loop through each column in the DataFrame
    if pd.api.types.is_numeric_dtype(data[column]):
        mean = data[column].mean()
        # Calculate the mean of the column
        median = data[column].median()
        # Calculate the median of the column
        # Print the mean and median
        print(f"{column}: mean = {mean}, median = {median}")
