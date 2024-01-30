import pandas as pd
from sqlalchemy import create_engine

# create dataframe
row_df = pd.read_excel('./datafiles/slots_and_names.xlsx')
df = row_df.iloc[3:]
df.reindex
df.columns = ['slots', 'a', 'name']
df = df[['slots', 'name']]
df[['garden', 'section', 'lot', 'block', 'space']] = df['slots'].str.split(', ', expand=True)
print(df.head())
print(df.columns)
print(df.iloc[3])

# populate databse
engine = create_engine("mysql+mysqlconnector://root:root@localhost/cemetry_service")
df.to_sql('burials', con=engine, if_exists='append', index=False)