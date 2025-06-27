import pandas as pd

#exercise2 question 5
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

input(reviews)
reviews_means= reviews.price.mean()
centered_price= reviews.price - reviews_means
input(centered_price)