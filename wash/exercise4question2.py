import pandas as pd

#exercise4 question 2 提取酒的价格，并将其从大到小排序

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)

best_rating_per_price = reviews.groupby(by='price',dropna=True,as_index=True).points.max()
print(best_rating_per_price)