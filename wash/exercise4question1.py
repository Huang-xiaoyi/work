import pandas as pd

#exercise4 question 1 目标要求计算出每个品酒人的评价贡献量，并将结果制作成
  #以taster_twitter_handle为name的Series
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews)
reviews_written= reviews.groupby('taster_twitter_handle').taster_name.count()
reviews_written = reviews_written.rename('taster_twitter_handle')
print(reviews_written)