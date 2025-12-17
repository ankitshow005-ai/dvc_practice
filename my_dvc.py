import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Sanjoy/Practice/dvc_practice/data_location/raw_data.csv')

# cat_col = [col for col in df.columns if df[col].dtype == 'O'] 
# num_col = [col for col in df.columns if df[col].dtype != 'O']

# print(f'{cat_col}, {num_col}') 

data = pd.DataFrame({'name': ['Ankit'], 'age': [23], 'city': ['Kolkata']})
print(data)

new_df = pd.concat([df,data], ignore_index = True)
print(new_df)

new_df.to_csv("data_location/raw_data_modified.csv", index=False)

