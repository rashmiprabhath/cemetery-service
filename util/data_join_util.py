import pandas as pd

slots_and_names = pd.read_parquet('../datafiles/slots_and_names.parquet.gzip')
slots_and_dates = pd.read_parquet('../datafiles/burials_and_dates.parquet.gzip')
print(len(slots_and_names.index))
print(len(slots_and_dates.index))

df = pd.merge(slots_and_dates, slots_and_names, on='slots')

df.to_parquet('merged.parquet.gzip', compression='gzip')
print(df[['name','birth_date']].head(100))