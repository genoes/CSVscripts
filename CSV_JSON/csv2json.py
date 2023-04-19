import pandas as pd

path = input('\n'"Enter absolute path to CSV file: "'\n').strip()

# Load the JSON file into a pandas DataFrame
df = pd.read_csv(path)

# Convert the DataFrame to CSV format and save it to a file
df.to_json('output.json',  orient='records', indent=4)
print('\n''''
  ___                 ___  
 (o o)               (o o) 
(  V  )  COMPLETE!  (  V  )
--m-m-----------------m-m--
'''
'\n')



