import pandas as pd

df = pd.read_parquet('../datafiles/merged.parquet.gzip')
df.to_excel("../datafiles/result.xlsx", sheet_name='Sheet_name_1')