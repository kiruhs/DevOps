import pandas as pd
import numpy as np # array
from tabulate import tabulate
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sys

from time import sleep
# Series - 1-dimension
# DataFrame - 2-dimension

# series = pd.Series([1, 2, 3] , index=['a','b','c'])
# print(series['a'])
# print(series.index)

# series2 = pd.Series(["Ferrari", "Ferrari", "Lamborghini"], index=[1, 2, 3])
# # print(series2)
# # print(series2.info())
# print(series2.describe())

# s1 = pd.Series(['200', '140','python', '-210.34', '400'])
# print(type(s1[0]))
# print(s1)
# s2 = pd.to_numeric(s1, errors='coerce')
# # print(s2)
# s3 = s2.sort_values(ascending=False)
# print(s3)
# s4 = s3.dropna()
# print(s4)

# s1 = pd.Series([1, 2, 3, 4, 5])
# s2 = pd.Series([2, 4, 6, 8, 10])

# print("Print items from first series that are not presented in the second one: ")
# res = s1[~s1.isin(s2)]
# print(res.index)

# s11 = pd.Series(np.union1d(s1, s2))
# # print(s11)  # union
# s22 = pd.Series(np.intersect1d(s1, s2))
# # print(s22)
# print("Print all items of given series that are not presented in another")
#
# res = s11[~s11.isin(s22)]
# print(res)
# print(pd.Series(np.setdiff1d(s11, s22)))

# df = pd.DataFrame([[1, "John", 5.0], [2, "Bob", 4.3], [3, "Mary", 4.5]], columns=["Num", "Name", "Score"])
# print(df)
# # print(df["Name"])
# print(df.Score)
# print(df["Score"].name)
# url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita"
# tbls = pd.read_html(url, encoding='utf-8')
# print(type(tbls))
# print(tbls[1])
# print(tbls[1].to_string(index=False, max_colwidth=20, max_rows=30))
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10)
# print(tbls[1])

# df = pd.read_csv('test.csv', encoding='utf-8')
# print(df.loc[2, 'col7'])
# print(df.col7)
# df['col7'] = df['col7'].str.replace(',', '')
# df['col6'] = df['col6'].str.replace(',', '')

# df.loc[1:, 'col7'] = df.loc[1:, 'col7'].str.strip('"').astype(float)
# df.loc[1:, 'col4'] = df.loc[1:, 'col4'].str.strip('"').astype(float)
# df.loc[1:, 'col6'] = df.loc[1:, 'col6'].str.strip('"').astype(float)
# df.loc[1:, 'col5'] = df.loc[1:, 'col5'].str.strip('"%').astype(float)/100

# print(df.col7)
# print(type(df.loc[1, 'col7']))
# df1 = df.loc[1:][df.loc[1:, 'col7'] > 3000]
# print(df1)

# print(tabulate(df1, headers=df.iloc[0], tablefmt='psql', showindex=False))

# print(df1.col5.mean())
# print(df1.col7.sum())
# print(df1.col4.max())

# print(df1.groupby('col4').col7.sum())
# print(df1.groupby('col4').col7.mean())
# print(df1.groupby('col4').col7.std())

# df1.col7.plot()
# df1.col4.plot()
# df1.col5.plot()
# df1.col6.plot()
# sns.histplot(data=df1, x='col4')
# sns.scatterplot(data=df1, x='col4', y='col5', hue='col6')
# plt.show()
# plt.savefig("stocks.png")
# sys.stdout.flush()

exam_data = {'name': ['John', 'Tom', 'Bob', ' Mary', 'Sarah', 'Michael'],
             'score': [12.5, 9, 16.3, np.nan, 9, 20],
             'attempts': [1, 3, 3, 2, 1, 2],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f']
df = pd.DataFrame(exam_data, index=labels)
# print("Original rows:")
# print(df)
# print("Append a new row:")
# df.loc['z'] = ['Alex', 15.5, 2, 'yes']
# print(df)
print("Delete some row:")
df.drop('f', inplace=True)
print(df)
df2 = {'name':'Alex', 'score': 15.5, 'attempts': 2, 'qualify': 'yes'}
df = df._append(df2, ignore_index=True)
print(df)