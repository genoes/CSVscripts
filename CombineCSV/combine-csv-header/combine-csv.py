import pandas as pd
import glob

# Define the CSV directory
path = input('\n'"Enter absolute path to CSV directory: "'\n').strip()

all_files = glob.glob(path + '/*.csv')

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col = None, header = 0)
    li.append(df)

# Combine the dfs, matching columns and filling missing values with NaN
combined_df = pd.concat(li, axis = 0, ignore_index = True, sort = False)

# Reorder the columns alphabetically
# combined_df = combined_df.reindex(sorted(combined_df.columns), axis = 1)

# Write the combined df to a new CSV file
combined_df.to_csv('combined_sheet.csv', index = False, encoding = 'utf-8')
print('\n''''
  ___                 ___  
 (o o)               (o o) 
(  V  )  COMPLETE!  (  V  )
--m-m-----------------m-m--
'''
'\n')
