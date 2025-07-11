import pandas as pd

#exercise4 question 3 要求获取每个种类中价格最低和最高的酒

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)

max_price = reviews.groupby(by='variety').price.max().rename('max')
min_price = reviews.groupby(by='variety').price.min().rename('min')
price_extremes = pd.concat([min_price, max_price], axis=1,join='inner')

print(price_extremes)

