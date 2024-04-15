import pandas as pd
df = pd.read_excel('q.xlsx')
df['Company'] = df['name'].str.split().str[0]
df.drop(columns=['name'],inplace=True)
df.rename(columns={'Company':'name'},inplace=True)
df.to_excel('a.xlsx',index=False)