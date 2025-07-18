import pandas as pd

#exercise5 question 2 建立一个Series，是酒表的points列的字符串版本

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)

point_strings = reviews.points.astype('str')

print(point_strings)