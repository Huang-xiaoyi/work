import pandas as pd

#exercise2 question 5
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

def best_pt2pr(re):
    re.points = re.points / re.price
    return re.sort_index(axis=0, ascending=True, na_position=1)

input(reviews)
bargain_position = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_position, 'title']
input(bargain_wine)