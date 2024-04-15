import pandas as pd
df = pd.read_excel("dat.xlsx","Orders")
ans1  = df["Category"].unique()
print(ans1)

ans2 = df["Category"].value_counts()
print(ans2)

ans3 = df["Sub-Category"].value_counts()
print(ans3)


ans5 = df[df["Category"] == "Office Supplies"]
count1 = df["Sub-Category"].value_counts()
count2 = len(df["Category"] == "Office Supplies")
percentage_distribution1 = (count1 / count2) * 100
print(percentage_distribution1)

ans6 = df[df["Category"] == "Technology"]
count1 = df["Sub-Category"].value_counts()
count2 = len(df["Category"] == "Technology")
percentage_distribution2 = (count1 / count2) * 100
print(percentage_distribution2)

ans7 = df[df["Category"] == "Technology"]
count1 = df["Sub-Category"].value_counts()
count2 = len(df["Category"] == "Technology")
percentage_distribution3 = (count1 / count2) * 100
print(percentage_distribution3)

ans8 = df.groupby("Sub-Category")[["Profit", "Sales"]].sum()
print(ans8)

ans9 = df["Products"].unique.count()
print(ans9)

ans10 = df.groupby("Products")["Orders"].value_counts()
print(ans10)

ans11 = df.group("Sub-Category")["Region"].value_counts()
print(ans11)

ans12 = df.sort_values("Profit", ascending = False)
print(ans12[1])

ans13 = df["Sub-Category"].sort_values("Profit", ascending = False)
print(ans13[1])

ans14 = df.sort_values("Profit", ascending = True)
print(ans14[1])

ans15 = df.sort_values("Profit", ascending = True)
print(ans15[1])

ans16 = df["Customer"].sort_values("Orders", ascending=False)
print(ans16[1:10])

ans17 = df["Customer"].unique.count()
print(ans17)

ans18 = df["Customer","New York"].sort_values["Profit", ascending = False]
print(ans18[1:10])

ans19 = df["Product"].sort_values["Ship Date"-"Order Date", ascending = False]
print(ans19[1:10])


