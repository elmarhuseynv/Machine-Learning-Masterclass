# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv('Sales_Funnel_CRM.csv')

# %%
df

# %%
licenses = df[['Company','Product','Licenses']]
licenses

# %%
pd.pivot(data=licenses,index='Company',columns='Product',values='Licenses')

# %%
pd.pivot_table(df,index="Company",aggfunc='sum')

# %%
pd.pivot_table(df,index="Company",aggfunc='sum')[['Licenses','Sale Price']]

# %%
pd.pivot_table(df,index="Company",aggfunc='sum',values=['Licenses','Sale Price'])

# %%
df.groupby('Company').sum()[['Licenses','Sale Price']]

# %%
pd.pivot_table(df,index=["Account Manager","Contact"],values=['Sale Price'],aggfunc='sum')

# %%
pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price"],columns=["Product"],aggfunc=[np.sum],fill_value=0)

# %%
# Can add multiple agg functions
pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price"],columns=["Product"],
               aggfunc=[np.sum,np.mean],fill_value=0)

# %%
# Can add on multiple columns
pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price","Licenses"],columns=["Product"],
               aggfunc=[np.sum],fill_value=0)


