import pandas as pd

#exercise4 question 6 创建一个Series索引是[country, variety]，并且按葡萄酒计数排序

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)

country_variety_counts = reviews.groupby(by=['country', 
                                             'variety']).count().winery.sort_values(ascending=False)

print(country_variety_counts)