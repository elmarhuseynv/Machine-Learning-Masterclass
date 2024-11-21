# %%
import numpy as np
import pandas as pd

from datetime import datetime

# %%
my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15

# %%
my_date = datetime(my_year,my_month,my_day)

# %%
myser = pd.Series(["Jul 31, 2009", "Jan 10, 2010", None])

# %%
myser

# %%
pd.to_datetime(myser)

# %%
pd.to_datetime(myser)[0]

# %%
style_date = '12--Dec--2000'

# %%
pd.to_datetime(style_date, format='%d--%b--%Y')

# %%
strange_date = '12th of Dec 2000'

# %%
pd.to_datetime(strange_date)

# %%
sales = pd.read_csv('RetailSales_BeerWineLiquor.csv')

# %%
sales

# %%
sales['DATE'] = pd.to_datetime(sales['DATE'])

# %%
sales

# %%
sales = pd.read_csv('RetailSales_BeerWineLiquor.csv',parse_dates=[0])

# %%
sales

# %%
sales = sales.set_index("DATE")

# %%
sales.resample(rule='A').mean()

# %%



