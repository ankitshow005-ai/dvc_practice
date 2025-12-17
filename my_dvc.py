import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Sanjoy/Practice/dvc_practice/data_location/raw_data.csv')
git 
cat_col = [col for col in df.columns if df[col].dtype == 'O'] 
num_col = [col for col in df.columns if df[col].dtype != 'O']

print(cat_col, num_col)