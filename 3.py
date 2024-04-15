
import pandas as pd
df = pd.read_excel("Bookshop.xlsx","Author")
ans1 = df["Country of Residence"]
s = ans1.sort_values()
print(s.max(3))
