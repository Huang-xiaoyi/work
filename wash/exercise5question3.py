import pandas as pd

#exercise5 question 3 找出有多少条记录缺失了价格，这里价格要与酒绑定，因此计数后提取酒这一列

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)

n_missing_prices = reviews[pd.isnull(reviews.price)].count().winery
print(n_missing_prices)