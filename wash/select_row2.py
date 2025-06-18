import pandas as pd

#exercise2 question 4
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

input(reviews)
first_descriptions = reviews.loc[0:9, 'description']
input(first_descriptions)