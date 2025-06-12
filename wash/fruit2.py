import pandas as pd

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruit_sales = pd.DataFrame({
    'Apples': [35, 41],
    'Bananas': [21, 34]
}, index=['2017 Sales', '2018 Sales'])
# Check your answer
# q1.check()
input(fruit_sales)