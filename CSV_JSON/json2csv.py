import pandas as pd

path = input('\n'"Enter absolute path to JSON file: "'\n').strip()

# Load the JSON file into a pandas DataFrame
df = pd.read_json(path)

# Convert the DataFrame to CSV format and save it to a file
df.to_csv('output.csv', index=False, encoding = 'utf-8')
print('\n''''
  ___                 ___  
 (o o)               (o o) 
(  V  )  COMPLETE!  (  V  )
--m-m-----------------m-m--
'''
'\n')