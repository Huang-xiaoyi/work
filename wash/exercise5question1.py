import pandas as pd

#exercise5 question 1 要求获得points列的数据类型

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)

dtype = reviews.points.dtype

print(dtype)