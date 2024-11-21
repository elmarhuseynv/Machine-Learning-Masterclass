# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('dm_office_sales.csv')

# %%
df.head()

# %%
plt.figure(figsize=(5,8), dpi=100)

sns.rugplot(x='salary', data=df, height=0.5)

# %%
plt.figure(figsize=(10, 5), dpi=100)

sns.displot(data=df, x='salary', bins=20, color='red', edgecolor='blue')

# %%
sns.histplot(data=df, x='salary')

# %%
sns.kdeplot(data=df, x='salary')

# %%
np.random.seed(42)
sample_ages = np.random.randint(0,100, 200)

# %%
sample_ages = pd.DataFrame(sample_ages, columns=['ages'])

# %%
sample_ages.head()

# %%
sns.displot(data=sample_ages, x= 'ages', rug=True, bins=30, kde=True)

# %%
sns.kdeplot(data=sample_ages, x='ages', clip=[0,100], shade=True)

# %%



