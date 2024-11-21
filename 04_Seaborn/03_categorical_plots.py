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
df['division'].value_counts()

# %%
plt.figure(figsize=(10, 4), dpi=200)
sns.countplot(data=df, x='division')
plt.ylim(90, 260)

# %%
df['level of education'].value_counts()

# %%
plt.figure(figsize=(10, 4), dpi=200)
sns.countplot(data=df, x='level of education')

# %%
plt.figure(figsize=(10, 4), dpi=200)
sns.countplot(data=df, x='level of education', hue='division', palette='Set2')

# %%
plt.figure(figsize=(10, 6), dpi=200)
sns.barplot(data=df, x='level of education', y='salary', estimator=np.mean, ci='sd',
            hue='division')

plt.legend(bbox_to_anchor=(1.05, 1))

# %% [markdown]
# # Boxplot

# %%
df = pd.read_csv('StudentsPerformance.csv')

# %%
df.head()

# %%
plt.figure(figsize=(10, 4), dpi=200)
sns.boxplot(data=df, y='reading score', x='parental level of education', hue='test preparation course',
            palette='Set2')

plt.legend(bbox_to_anchor=(1.05, 1))

# %%
plt.figure(figsize=(10, 8), dpi=200)
sns.violinplot(data=df, x='reading score', y='parental level of education', hue='test preparation course',
            palette='Set2')

plt.legend(bbox_to_anchor=(1.55, 0.55))

# %%



