import pandas as pd

#exercise2 question 5
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

input(reviews)
top_oceania_wines = reviews.loc[((reviews.country == 'Australia')| (reviews.country =='New Zealand')) & (reviews.points >= 95)]
input(top_oceania_wines)