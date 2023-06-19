#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[7]:


fn = "2_Condition_Short.xlsx"
df = pd.read_excel(os.path.join("templates", fn))
sorted_df = df.sort_values(by=['CSName','UCSName'])
print(sorted_df)


# In[8]:


df.value_counts()


# In[9]:


df1 = pd.DataFrame(columns=df.columns)
df2 = pd.DataFrame(columns=df.columns)
for i in range(len(df)):
    # print(sorted_df.iloc[i])
    # print(type(sorted_df.iloc[i]))
    if i % 2 == 0:
        df1.loc[i // 2] = sorted_df.iloc[i]
    else:
        df2.loc[i // 2] = sorted_df.iloc[i]


# In[10]:


while df1[df1['UCSName'] == "Stimuli/Neg.BMP"].index[0] < df1[df1['UCSName'] == "Stimuli/Neg_UCS.BMP"].index[0] \
    or df1[df1['UCSName'] == "Stimuli/Pos.BMP"].index[0] < df1[df1['UCSName'] == "Stimuli/Pos_UCS.BMP"].index[0]:
    df1 = df1.sample(frac=1).reset_index(drop=True)
while df2[df2['UCSName'] == "Stimuli/Neg.BMP"].index[0] < df2[df2['UCSName'] == "Stimuli/Neg_UCS.BMP"].index[0] \
    or df2[df2['UCSName'] == "Stimuli/Pos.BMP"].index[0] < df2[df2['UCSName'] == "Stimuli/Pos_UCS.BMP"].index[0]:
    df2 = df2.sample(frac=1).reset_index(drop=True)
new_df = pd.concat([df1, df2], axis=0)
# new_df = new_df.drop(columns=["index"])
# new_df = new_df.droplevel(0, axis=1) 


# In[11]:


new_df.to_excel(fn, index=False)


# In[ ]:




