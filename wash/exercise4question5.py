import pandas as pd

#exercise4 question 5 获取每个品酒师给过的平均分值

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)

reviewer_mean_ratings = reviews.groupby(by='taster_name').points.mean()

print(reviewer_mean_ratings)