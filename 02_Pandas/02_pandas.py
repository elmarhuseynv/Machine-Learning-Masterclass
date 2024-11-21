# %%
import pandas as pd
import numpy as np

# %% [markdown]
# ### Series

# %%
myindex= ['USA', 'Canada', 'Mexico']

# %%
mydata = [1884, 2014, 1798]

# %%
myser = pd.Series(data=mydata, index = myindex)

# %%
myser

# %%
myser[0]

# %%
ages = {'Sam':5, 'Jack':6, 'Mia':7, 'Ron':4}
ages1 = {'Sam':5, 'Jack':6, 'Mia':7, 'Rony':4}

# %%
ages = pd.Series(ages)
ages1 = pd.Series(ages1)

# %%
ages

# %%
ages['Ron']

# %%
ages1 = ages * 4

# %%
ages1

# %%
ages + ages1

# %%
ages.add(ages1, fill_value=0)

# %% [markdown]
# ### Data Frames

# %%
np.random.seed(101)
mydata = np.random.randint(0, 101, (4,3))

# %%
mydata

# %%
myindex = ["CA", 'NY', 'AZ', 'TX']

# %%
mycolumns = ['Jan', 'Feb', 'Mar']

# %%
df = pd.DataFrame(mydata, index=myindex, columns=mycolumns)

# %%
df

# %%
df.info()

# %%
tips = pd.read_csv('tips.csv')

# %%
tips

# %%
tips.columns

# %%
tips.index

# %%
tips.head()

# %%
tips.tail()

# %%
tips.info()

# %%
tips.describe()

# %% [markdown]
# ### Columns

# %%
tips.head()

# %%
tips['total_bill']

# %%
type(tips['total_bill'])

# %%
tips[['total_bill', 'tip']]

# %%
tips['tip_percentage'] = 100 * tips['tip'] / tips['total_bill']

# %%
tips.head()

# %%
tips['price_per_person'] = tips['total_bill'] / tips['size']

# %%
tips.head()

# %%
tips['price_per_person'] = np.round(tips['total_bill'] / tips['size'], 2)

# %%
tips.head()

# %%
tips.drop('tip_percentage', axis=1)

# %%
tips.shape

# %% [markdown]
# ### Rows

# %%
tips.index

# %%
df = tips.set_index('Payment ID')

# %%
df.head()

# %%
df.reset_index()

# %%
df.iloc[0]

# %%
df.loc['Sun2959']

# %%
df.loc[['Sun2959', 'Sun2251']]

# %%
df.drop('Sun2959', axis=0)

# %% [markdown]
# ### Conditional Filtering

# %%
df = pd.read_csv("tips.csv")

# %%
df.head()

# %%
bool_series = df['total_bill'] > 40

# %%
df[bool_series]

# %%
df[df['size'] > 3]

# %%
df['total_bill'] > 30

df['sex'] == 'Male'

# %%
df[(df['total_bill'] > 30) & (df['sex'] == 'Male')]

# %% [markdown]
# ### Useful Methods

# %%
df = pd.read_csv('tips.csv')

# %%
df.head()

# %%
df.info()

# %%
def last_four(num):
    return str(num)[-4:]

# %%
df['last_four'] = df['CC Number'].apply(last_four)

# %%
df.head()

# %%
def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price<30:
        return '$$'
    else:
        return '$$$'

# %%
df['yelp'] = df['total_bill'].apply(yelp)

# %%
df.head()

# %%
def quality(total_bill, tip):
    if tip/total_bill < 0.25:
        return "Generous Tip"
    else: 
        return "Other"

# %%
df['Tip Quality'] = df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'],df['tip']),axis=1)

# %%
df.head()

# %%
df['Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])

# %%
df.head()

# %%
import timeit

# %%
setup = '''
import numpy as np
import pandas as pd
df = pd.read_csv('tips.csv')
def quality(total_bill,tip):
    if tip/total_bill  > 0.25:
        return "Generous"
    else:
        return "Other"
'''
  
# code snippet whose execution time is to be measured 
stmt_one = ''' 
df['Tip Quality'] = df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'],df['tip']),axis=1)
'''

stmt_two = '''
df['Tip Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
'''

# %%
timeit.timeit(setup = setup, 
                    stmt = stmt_one, 
                    number = 1000) 

# %%
timeit.timeit(setup = setup, 
                    stmt = stmt_two, 
                    number = 1000)

# %% [markdown]
# ### Missing Data

# %%
df = pd.read_csv('movie_scores.csv')

# %%
df.head(15)

# %%
df.isnull()

# %%
df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())]

# %%
df.dropna(thresh=2)

# %%
df.fillna('new value!')

# %%
df['pre_movie_score'] = df['pre_movie_score'].fillna(0)

# %%
df['pre_movie_score'].fillna(df['pre_movie_score'].mean())

# %%
airline_tix = {'first':100,'business':np.nan,'economy-plus':50,'economy':30}
ser = pd.Series(airline_tix)

# %%
ser

# %%
ser.interpolate()

# %% [markdown]
# ### GroupBy Operations

# %%
df = pd.read_csv('mpg.csv')

# %%
df.head()

# %%
df.info()

# %%
df = df.drop('horsepower', axis=1)

# %%
df = df.drop('name', axis=1)

# %%
df['model_year'].value_counts()

# %%
avg_year = df.groupby('model_year').mean()

# %%
avg_year.index

# %%
avg_year.columns

# %%
avg_year['mpg']

# %%
df.groupby(['mpg', 'cylinders']).mean()

# %%
df.groupby('model_year').describe()

# %%
df.groupby(['model_year','cylinders']).mean()

# %%
df.groupby(['model_year','cylinders']).mean().index

# %%
year_cyl = df.groupby(['model_year','cylinders']).mean()

# %%
year_cyl.loc[70]

# %%


# %%


# %% [markdown]
# ### Combining DataFrames

# %%
df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])

# %%
df1

# %%
df2 = pd.DataFrame([['c', 3], ['d', 4]],
                   columns=['letter', 'number'])

# %%
df2

# %%
mydf = pd.concat([df1, df2], axis=0)

# %%
mydf.index = range(len(mydf))

# %%
mydf

# %%
data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29]
}

df1 = pd.DataFrame(data1)

# %%
data2 = {
    'ID': [3, 4, 5, 6, 7],
    'Country': ['USA', 'UK', 'Germany', 'France', 'Spain'],
    'Score': [85, 90, 78, 92, 88]
}
df2 = pd.DataFrame(data2)

# %%
df1

# %%
df2

# %%
#help(pd.merge)

# %%
pd.merge(df1, df2, how = 'inner', on='ID')

# %%
pd.merge(left=df1,right= df2, how = 'left', on='ID')

# %%
pd.merge(left=df1,right= df2, how = 'right', on='ID')

# %%
pd.merge(df1, df2, how='outer', on='ID')

# %%
df1 = df1.set_index("ID")

# %%
df1

# %%
pd.merge(left=df1,right= df2, left_index=True, right_on="ID")

# %% [markdown]
# ### Text Methods for String Data

# %%
email = 'murphy@email.com'

# %%
email.split('@')

# %%
names = pd.Series(['andrew', 'bob', 'mavis', 'damiano', '5'])

# %%
names

# %%
names.str.upper()

# %%
email.isdigit()

# %%
'5'.isdigit()

# %%
names.str.isdigit()

# %%
tech_finance = ['GOOG,APPL,AMZN','JPM,BAC,GS']

# %%
tickers = pd.Series(tech_finance)

# %%
tickers.str.split(',')

# %%
tickers.str.split(',').str[0]

# %%
tickers.str.split(',',expand=True)

# %%
messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])

# %%
messy_names

# %%
messy_names.str.replace(';', "").str.strip().str.capitalize()

# %%
def cleanup(name):
    name = name.replace(";","")
    name = name.strip()
    name = name.capitalize()
    return name

# %%
messy_names.apply(cleanup)


