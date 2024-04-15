# -*- coding: utf-8 -*-
"""Copy of notebookf0aef8686b

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZjUiXvCmc5PlNWiO8KIUS7gN2tYuQ38Y
"""

!pip install gdown
!gdown --id 1eHChVwaAwG66p9eDhISOROPIvKXnMg9W

from zipfile import ZipFile
with ZipFile("/content/Arjun_Assignment_data-20220427T165022Z-002.zip", 'r') as zObject:
	zObject.extractall(
		path="/content/Arjun_Assignment_data-20220427T165022Z-002")

from zipfile import ZipFile
with ZipFile("/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001.zip", 'r') as zObject:
	zObject.extractall(
		path="/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001")

from zipfile import ZipFile
with ZipFile("/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-002.zip", 'r') as zObject:
	zObject.extractall(
		path="/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-002")

from zipfile import ZipFile
with ZipFile("/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-003.zip", 'r') as zObject:
	zObject.extractall(
		path="/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-003")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from collections import Counter

D1_postlinks = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001/dataset/postLinks.csv')
print(D1_postlinks)

D1_postlongs = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001/dataset/posts_long.csv')
print(D1_postlongs.columns)

D1_postshort = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001/dataset/posts_short.csv')
print(D1_postshort.columns)

D1_postlinks_json = pd.read_json('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001/dataset/postLinks.json')
print(D1_postlinks_json.columns)

D2_User = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-002/dataset/users.csv')
print(D2_User.columns)

D2_postslong_json = pd.read_json('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-002/dataset/posts_long.json')
print(D2_postslong_json.columns)

D3_post_history = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-003/dataset/post_history.csv')
print(D3_post_history.columns)
print(D3_post_history)

D1_postlinks = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001/dataset/postLinks.csv')
D1_postlongs = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001/dataset/posts_long.csv')
D1_postshort = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001/dataset/posts_short.csv')
D1_postlinks_json = pd.read_json('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-001/dataset/postLinks.json')
D2_postslong_json = pd.read_json('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-002/dataset/posts_long.json')
D2_User = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-002/dataset/users.csv')
D3_post_history = pd.read_csv('/content/Arjun_Assignment_data-20220427T165022Z-002/Arjun_Assignment_data/dataset-20210607T020316Z-003/dataset/post_history.csv')

# Question 1 :- Determine the Number of Tags Per Question

Q1_DS = pd.concat([D1_postlongs[['id' , 'tags']] , D1_postshort[['id' , 'tags']] , D2_postslong_json[['id' , 'tags']]])
no_of_tags = []
for tag in Q1_DS['tags'] :
  tags = re.findall(r'<.*?>', tag)
  no_of_tags.append(len(tags))
Q1_DS['No_of_Tags'] = no_of_tags
Q1_ANS = Q1_DS[['id' , 'No_of_Tags']]
print(Q1_DS)

Q2_DS = pd.concat([D1_postlongs[['id' , 'tags']] , D1_postshort[['id' , 'tags']] , D2_postslong_json[['id' , 'tags']]])
total_tags = []
for tag in Q2_DS['tags'] :
  tags = re.findall(r'<.*?>', tag)
  total_tags.extend(tags)

total_tags = pd.Series(total_tags)
print(total_tags.nunique())

# Question - 3 :-Determine the top-25 Tags appearing frequently

Q3_DS = pd.concat([D1_postlongs[['id', 'tags']], D1_postshort[['id', 'tags']], D2_postslong_json[['id', 'tags']]])

total_tags = []

for tag in Q3_DS['tags']:
    tags = re.findall(r'<.*?>', tag)
    total_tags.extend(tags)

total_tags_series = pd.Series(total_tags)
tag_frequency = total_tags_series.value_counts()
frequency_df = pd.DataFrame({'Tag': tag_frequency.index, 'Frequency': tag_frequency.values})

Q3_Ans = frequency_df.head(25)
print(Q3_Ans)

Q4_Ans = frequency_df.head(500)
plt.figure(figsize=(50, 25))
plt.plot(Q4_Ans['Tag'], Q4_Ans['Frequency'], marker='o', linestyle='-')
plt.xlabel('Tag')
plt.ylabel('Frequency')
plt.title('Top 500 Tags Frequency Distribution')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

Q_5_DS = pd.merge(D3_post_history, D1_postlinks, on='id')
filtered_Q_5_DS = Q_5_DS[Q_5_DS['ph_type_id'] == 3]
filtered_Q_5_DS['creation_date_x'] = pd.to_datetime(filtered_Q_5_DS['creation_date_x'])
filtered_Q_5_DS["Year"] = filtered_Q_5_DS["creation_date_x"].dt.year
filtered_Q_5_DS["Month"] = filtered_Q_5_DS["creation_date_x"].dt.month
Q5_Ans = filtered_Q_5_DS.groupby(['Year', 'Month'])['creation_date_x'].count().reset_index(name='counts')
total_counts = Q5_Ans['counts'].sum()
Q5_Ans['relative_frequency'] = (Q5_Ans['counts'] / total_counts) * 100
plt.figure(figsize=(50, 25))
plt.plot(Q5_Ans['Year'].astype(str) + '-' + Q5_Ans['Month'].astype(str), Q5_Ans['counts'], marker='o', linestyle='-')
plt.xlabel('Month-Year')
plt.ylabel('Counts')
plt.title('Counts of Posts by Month-Year')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Question 6

Q6_DS = pd.concat([D1_postlongs[['id', 'tags']], D1_postshort[['id', 'tags']], D2_postslong_json[['id', 'tags']]])
Q6_DS = pd.merge(Q6_DS , D3_post_history , on = 'id')
total_tags = []

for tag in Q6_DS['tags']:
    tags = re.findall(r'<.*?>', tag)
    total_tags.append(tags)

Q6_DS['tags_diff'] = total_tags
Q6_DS = Q6_DS[Q6_DS['ph_type_id'] == 3]
print(Q6_DS.columns)
flattened_tags = [tag for sublist in Q6_DS['tags_diff'] for tag in sublist]
tag_counts = Counter(flattened_tags)
tag_counts_df = pd.DataFrame(tag_counts.items(), columns=['Tag', 'Count'])
total_tags_count = tag_counts_df['Count'].sum()
tag_counts_df['Percentage'] = (tag_counts_df['Count'] / total_tags_count) * 100
tag_counts_df = tag_counts_df.sort_values(by='Count', ascending=False)
top_20 = tag_counts_df[:20]

# Plotting
plt.figure(figsize=(50, 25))
plt.bar(top_20['Tag'], top_20['Percentage'], color='blue', alpha=0.7)

for i, value in enumerate(top_20['Percentage']):
    plt.text(i, value, str(value), ha='center', va='bottom', weight='bold')

plt.xlabel('Tag')
plt.ylabel('Percentage')
plt.title('Tag Percentage')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Question - 7

Q7_DS = pd.concat([D1_postlongs, D1_postshort])
Q7_DS = pd.merge(Q7_DS , D3_post_history , on = 'id')
Q7_DS = pd.merge(Q7_DS, D1_postlinks , on = 'id')
Q7_DS = Q7_DS[Q7_DS['link_type_id'] == 3]
Q7_DS['creation_date'] = pd.to_datetime(Q7_DS['creation_date'])
Q7_DS['community_owned_date'] = pd.to_datetime(Q7_DS['community_owned_date'])
Q7_DS['close_time'] = Q7_DS['community_owned_date'] - Q7_DS['creation_date']
Q7_DS_Plot = Q7_DS[['id' , 'close_time']]
plt.figure(figsize=(10, 6))
bars = plt.bar(Q7_DS_Plot['id'], Q7_DS_Plot['close_time'].dt.days, color='blue', alpha=0.7)
plt.xlabel('Post ID')
plt.ylabel('Close Time (Days)')
plt.title('Close Time for Each Post')
plt.xticks(rotation=90)

for bar, time in zip(bars, Q7_DS_Plot['close_time'].dt.days):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(time), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Question - 8

#Q8
merge = pd.merge(D2_User, Q6_DS, on='id', how='inner')
dele = [ 'creation_date','display_name','views','upvotes','downvotes', 'tags', 'Unnamed: 0', 'ph_type_id', 'post_id', 'revision_guid', 'creation_date', 'comment', 'text', 'tags_diff']
merge = merge.drop(columns=dele)
print(merge)

merge = pd.merge(D2_User, Q6_DS, on='id', how='inner')
dele = [ 'display_name','views','upvotes','downvotes', 'tags', 'ph_type_id', 'post_id', 'revision_guid', 'creation_date', 'comment', 'text', 'tags_diff']
merge = merge.drop(columns=dele)
print(merge)

Q9 = D1_postlongs['community_owned_date'].iloc[:500].notnull().count()
print(Q9/5)

Q10 = D1_postlongs['community_owned_date'].iloc[:5000].notnull().count()
print(Q10/50)