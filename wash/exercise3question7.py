import pandas as pd

#exercise2 question 5
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

input(reviews)

def Grade(re):
    if re.country == 'Canada':
        return 3
    elif re.points >= 95:
        return 3
    elif  re.points>= 85:
        return 2
    elif re.points < 85:
        return 1

star_ratings = reviews.apply(Grade, axis='columns')
input(star_ratings)