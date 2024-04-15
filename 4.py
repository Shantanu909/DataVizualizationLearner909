import pandas as pd
df = pd.read_excel("Bookshop.xlsx","Author")
ans1 = df["Hrs Writing per Day"]
ans1.sort_values()
print(df["AuthID"].sortby(ans1.max))
