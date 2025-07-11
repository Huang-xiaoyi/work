import pandas as pd

#exercise4 question 4 基于上一个问题得到的DataFrame，将其按照各品种最低价格降序排序
# 最低价格相同时按最高价格降序排序

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)
# 1.获取副本
max_price = reviews.groupby(by='variety').price.max().rename('max')
min_price = reviews.groupby(by='variety').price.min().rename('min')
price_extremes = pd.concat([min_price, max_price], axis=1,join='inner')
# 2.根据种类的最低价格降序排序
sorted_varieties = price_extremes.sort_values(by=['min','max'],ascending=False)

print(sorted_varieties)