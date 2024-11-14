# from idlelib.iomenu import errors
import time

import pandas as pd
import numpy as np # array
# from tabulate import tabulate
# import matplotlib
# import matplotlib.pyplot as plt
# import seaborn as sns
import sys

from time import sleep

# from scipy.special import dtype

from bad import result

# from pandas import read_csv

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
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 10)
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

# exam_data = {'name': ['John', 'Tom', 'John', ' Mary', 'Sarah', 'Michael'],
#              'score': [12.5, 9, 16.3, np.nan, 9, 20],
#              'city': ['LA', 'NY', 'Boston', 'NY', 'Austin', 'Austin'],
#              'attempts': [1, 3, 3, 2, 1, 2],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f']
# df = pd.DataFrame(exam_data, index=labels)
# print("Original rows:")
# print(df)
# print("Append a new row:")
# df.loc['z'] = ['Alex', 15.5, 2, 'yes']
# print(df)
# print("Delete some row:")
# df.drop('f', inplace=True)
# print(df)
# df2 = {'name':'Alex', 'score': 15.5, 'attempts': 2, 'qualify': 'yes'}
# df = df._append(df2, ignore_index=True)
# print(df)

# class MyDF(pd.DataFrame):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for col in self.columns:
#             self[col] = self[col].str.replace('+', '')
#             self[col] = self[col].str.replace('2 5', '25')
#             self[col] = pd.to_numeric(self[col], errors='ignore')
#
# df = pd.read_csv("data.csv", encoding='utf-8')
# data = MyDF(df)
# print(type(df.loc[2,'phone']))
# print(type(data.loc[2,'phone']))
# print(data)
# print(df)
# df=df.sort_values([df.columns[0], df.columns[1]], ascending=True)
# print(df)

# g1 = df.groupby('city').size().reset_index(name='Number of people')
# print(g1)

# w_a_con = pd.read_csv("world_alcohol.csv")
# print(w_a_con)
# print(w_a_con.sample(5)) # choose 5 random rows
# print(w_a_con.sample(frac=0.1)) # fraction means part of all values when all values is 1
# print(w_a_con.drop_duplicates("WHO region").drop_duplicates('Beverage Types')) # drops all duplicates
# print(w_a_con.drop_duplicates("Beverage Types"))
# print(w_a_con[w_a_con['Country']=='Israel'])

# df = pd.DataFrame({
# 'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
# 'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
# 'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
# 'customer_id':['C3001','C3001','D3005','C3001','D3005','C3001','D3005','C3001','D3005','C3001','D3005','D3005'],
# 'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
# print(df)

# df_ag = df.groupby(['customer_id', 'salesman_id']).agg({'purch_amt':"sum"})
# print(df_ag)
# res = df_ag['purch_amt'].groupby(level=0, group_keys=False)
# print(res.nlargest())
# df['ord_date']=pd.to_datetime(df['ord_date'])
# res = df.groupby([df['ord_date'].dt.year, df['ord_date'].dt.month]).agg({'purch_amt':"sum"})
# print(res)

# res = (df.groupby(['salesman_id'])\
#        .agg(customer_id_start_C = ('customer_id', lambda x: sum(name.startswith('C') for name in x)),
#             # customer_id_list = ('customer_id', lambda x:','.join(x)),
#             customer_id_list = ('customer_id', lambda x:','.join(name for name in x if name.startswith('C'))),
#
#             purchase_amt_gap = ('purch_amt', lambda x: x.max() - x.min()))
       # .agg({'customer_id': "count",
       #      # 'customer_id': "lambda x: ','.join(x)",
       #      # customer_id_list = ('customer_id', lambda x:','.join(name for name in x if name.startswith('C'))),
       #      'purch_amt': "mean"})
       # )
# print(res)


# gr_data = df.groupby(['customer_id', 'salesman_id']).agg({'purch_amt': 'sum'})
# gr_data["%(Purch Amt.)"] = gr_data.apply(lambda x: 100*x/x.sum())
# print(gr_data)

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
# # print(df)
# def square(x):
#     return x**2
# df_squared = df.map(square)
# print(df_squared)
#
# df_rotate = df_squared.T
# print(df_rotate)
# df_counter_clock_wise = df_squared.T[::-1]
# print(df_counter_clock_wise)
# df_clock_wise = df_squared[::-1].T
# print(df_clock_wise)

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6]
# })

# Using iterrows (for method)
# for index, row in df.iterrows():
#     df.at[index,'C'] = row['A'] + row['B']
# df['C'](dtype='int16''int16')
# print(df)

# using apply()
# df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
# print(df)

# Vectorized addition
# df['C'] = df['A'] + df['B']
# print(df)

# Performance comparison
import timeit

# df = pd.DataFrame({'A': np.random.randint(1,100,100000),
#                    'B': np.random.randint(1,100,100000)})
#
# # Using iterrows (for method)
# def iterrows_add():
#     for index, row in df.iterrows():
#         df.at[index,'C'] = row['A'] + row['B']


# using apply()
# def apply_add():
#     df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
#
#
# # Vectorized addition
# def vectorized_add():
#     df['C'] = df['A'] + df['B']
#
# vectorized_time = timeit.timeit(vectorized_add, number=1)
# iterrows_time = timeit.timeit(iterrows_add, number=1)
# apply_time = timeit.timeit(apply_add,number=1)
#
# print(f"Vectorized time: {vectorized_time}")
# print(f"Iterrows time: {iterrows_time}")
# print(f"Apply time: {apply_time}")
# import time
# data = np.random.randint(1,1000, 7000000)
# df = pd.DataFrame(data, columns=['Values'])
# start = time.time()
# # for loop
# sum_for_loop = 0
# for value in df['Values']:
#     sum_for_loop += value
# time_for_loop = time.time() - start
#
# # sum built-in method
# start = time.time()
# sum_method = df['Values'].sum()
# time_sum_method = time.time() - start
#
# # results
# print("Sum using loop: ", sum_for_loop)
# print(f"Time using loop: {time_for_loop} seconds")
#
# print("Sum using sum method: ", sum_method)
# print(f"Time using sum: {time_sum_method} seconds")

lst = [i for i in range(1000000)]
start = time.time()
cnt = 0
for j in lst:
    cnt +=j
for_time = time.time() - start

start = time.time()
cnt2 = sum(lst)
sum_time = time.time() - start

print("Sum using loop: ", cnt)
print(f"Time using loop: {for_time} seconds")
#
print("Sum using sum method: ", cnt2)
print(f"Time using sum: {sum_time} seconds")
