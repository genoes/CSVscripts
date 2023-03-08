import pandas as pd
import glob

# Define the directory where the CSV files are located
path = input('\n'"Enter absolute path to CSV directory: "'\n').strip()
column_header = input('\n'"Enter column header you wish to concatenate by (e.g. Object identifier): "'\n').strip()

# Get a list of all the CSV files in the directory
all_files = glob.glob(path + "/*.csv")

# Initialize an empty list to store the DataFrames for each file
li = []

# Loop through each file and read it into a DataFrame
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)


# Combine the DataFrames, matching columns and filling missing values with NaN
combined_df = pd.concat(li, axis=0, ignore_index=True, sort=False)

# Group the rows by 'Object identifier' and concatenate the cells in each column
grouped_df = combined_df.groupby(column_header).agg(lambda x: ' | '.join(filter(lambda y: pd.notna(y) and str(y).strip() != '', set(x.astype(str).str.strip().values))))

# Delete all NaN values
grouped_df = grouped_df.replace('nan', '', regex=True)

# Reset the index to a continuous integer sequence
grouped_df = grouped_df.reset_index()

# Reorder the columns alphabetically
#grouped_df = grouped_df.reindex(sorted(grouped_df.columns), axis=1)

# Write the combined DataFrame to a new CSV file
grouped_df.to_csv("combined_sheet.csv", index=False, encoding = 'utf-8')
print('\n''''
  ___                 ___  
 (o o)               (o o) 
(  V  )  COMPLETE!  (  V  )
--m-m-----------------m-m--
'''
'\n')
