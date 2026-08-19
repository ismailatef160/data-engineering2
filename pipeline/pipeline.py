import sys
import pandas as pd
import os

print('arguments',sys.argv)

month = int(sys.argv[1])
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df['month'] = month
print(df.head())
os.makedirs('output', exist_ok=True)
df.to_parquet("output_12.parquet")

              

print(f'hello pipeline,month={month}')