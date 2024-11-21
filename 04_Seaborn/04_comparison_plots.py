# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('StudentsPerformance.csv')

# %%
df.head()

# %%
plt.figure(figsize=(10,4), dpi=200)
sns.jointplot(data=df, x='math score', y='reading score', kind='scatter', hue='gender')

# %%
sns.pairplot(data=df, hue='gender', diag_kind='hist')

# %%



