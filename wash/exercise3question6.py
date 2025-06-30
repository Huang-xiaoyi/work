import pandas as pd

#exercise2 question 5
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

input(reviews)
tropical_counts = reviews[reviews['description'].str.contains('tropical', na=False)]
fruity_counts = reviews[reviews['description'].str.contains('fruity', na=False)]
descriptor_counts = pd.Series([tropical_counts['description'].count(), fruity_counts['description'].count()],
                              index=['tropical', 'fruity'])
input(descriptor_counts)