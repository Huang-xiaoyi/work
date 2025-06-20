import pandas as pd

#exercise2 question 5
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

input(reviews)
italian_wines = reviews.loc[reviews.country == 'Italy']
input(italian_wines)