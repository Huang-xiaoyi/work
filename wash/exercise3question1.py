import pandas as pd

#exercise2 question 5
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

input(reviews)
median_points = reviews.points.median()
input(median_points)