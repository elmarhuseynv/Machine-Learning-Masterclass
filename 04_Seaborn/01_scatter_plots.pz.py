# %%
import pandas  as pd
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('dm_office_sales.csv')

# %%
df.head()

# %%
df.shape

# %%
plt.figure(figsize=(12,8), dpi=200)

sns.scatterplot(x='salary', y='sales', data=df, hue='level of education', palette='Dark2', size='work experience')

# %%
plt.figure(figsize=(12,4), dpi=200)

sns.scatterplot(x='salary', y='sales', data=df, s=80, style='level of education', hue='level of education')

#plt.savefig('my_plot.jpg')

# %%



