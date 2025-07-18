import pandas as pd

#exercise5 question 4 对酒出产地1的出品次数进行统计，空值用Unknow填充

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)

reviews_per_region = reviews.region_1.fillna('Unknow').value_counts().sort_values(ascending=False)
print(reviews_per_region)