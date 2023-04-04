#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


c=pd.read_csv(r"C:\Users\DELL\Desktop\Abhyaz_Task\data uplode\industry_india.csv")


# In[3]:


c


# In[4]:


# Extract columns A, B, and C
con = c[['Company Name','Email ID','Company Type']]


# In[5]:


con


# In[6]:


con.to_csv("C:\\Users\\DELL\\Desktop\\Abhyaz_Task\\data uplode\\contact_list.csv", index=False, header=True)


# In[7]:


con


# In[8]:


#drop numeric values from comapny name

con['Company Name'] =con['Company Name'].replace(to_replace=r'\d+',value='',regex=True)


# In[9]:


#drop all data if either mail or comapny name is null
p=con.dropna(subset=["Email ID", "Company Name"], inplace=True)


# In[10]:


con["Company Name"] = con["Company Name"].str.replace("fresher|FRESHER|Fresher|fRESHER|FResher|freshear|Fresheer|Freshes|None|none|NONE|NOne|abc|Abc", "")


# In[11]:


con.info()


# In[12]:


con = con[~((con['Company Type'].str.contains('None'))|(con['Company Type'].str.contains('none')))]


# In[13]:


con.to_csv("C:\\Users\\DELL\\Desktop\\Abhyaz_Task\\data uplode\\contact_list.csv", index=False, header=True)


# In[14]:


contact=pd.read_csv("C:\\Users\\DELL\\Desktop\\Abhyaz_Task\\data uplode\\contact_list_data.csv")


# In[15]:


contact.info()


# In[16]:


contact=contact.dropna(how="all")


# In[17]:


contact


# In[18]:


contact.info()


# In[19]:



contact.to_csv("C:\\Users\\DELL\\Desktop\\Abhyaz_Task\\data uplode\\contact_list_data.csv", index=False, header=True)


# In[20]:


#repalace speacial character which is at starting of name 
contact['Company Name'] = contact['Company Name'].str.replace(r'^[.,)(| .\/#?%_A$ & * ~ ` +  = : ;  . @ \ /]', '')


# In[21]:


contact['Company Name'] = contact['Company Name'].str.replace(r'^[. ]', '')


# In[22]:


contact['Company Name'] = contact['Company Name'].str.replace('[â€œÃ¢â‚¬Å“â€˜â€¢Ã¢â‚¬Â¢Ã¯Æ’ËœÂ·ÃÃ¯Æ’ÃŒÃ¯ÂÂ¶DÃ©]', '')


# In[69]:


l=pd.read_csv(r"C:\Users\DELL\Desktop\Abhyaz_Task\data uplode\contact_list_final.csv",encoding='ISO-8859-1')


# In[70]:


l.info()


# In[25]:


l['Company Name'] = l['Company Name'].str.replace(r"^'", "")


# In[88]:


#delete unwanted data based on keywords
l = l[~l['Company Name'].str.contains('jounior|senoir|assist|working|as a|as an|education|as |looking|pursuing|good|best|perfect|one of the|not |part time|parttime|searching|seeking|left |presently |recently|have a |jobless|right now|no ', case=False)]


# In[87]:


l.info()


# In[27]:


#delete those data which start with unwnated keywords.
l = l[~l['Company Name'].str.lower().str.startswith('charted')]
l = l[~l['Company Name'].str.lower().str.startswith('charted')]
l = l[~l['Company Name'].str.lower().str.startswith('charter')]


# In[28]:


l = l[~l['Company Name'].str.lower().str.startswith('assi')]
l = l[~l['Company Name'].str.lower().str.startswith('asis')]
l = l[~l['Company Name'].str.lower().str.startswith('jr.')]
l = l[~l['Company Name'].str.lower().str.startswith('admin')]
l = l[~l['Company Name'].str.lower().str.startswith('Consultant ')]
l = l[~l['Company Name'].str.lower().str.startswith('contsultancy')]


# In[29]:


l = l[~l['Company Name'].str.lower().str.startswith('consulate')]
l = l[~l['Company Name'].str.lower().str.startswith('consultent')]
l = l[~l['Company Name'].str.lower().str.startswith('ccou')]
l = l[~l['Company Name'].str.lower().str.startswith('ccen')]
l = l[~l['Company Name'].str.lower().str.startswith('ce ')]


# In[30]:


t=l.dropna(how='all')


# In[80]:


l.info()


# In[63]:


#drop all data if either mail or comapny name is null
#t=l.dropna(subset=["Email ID", "Company Name"], inplace=True)


# In[89]:


l.info()


# In[35]:


l.info()


# In[36]:


l


# In[ ]:





# In[37]:


l['Company Name'] = l['Company Name'].str.replace(r'^[.&`~* ]', '')


# In[83]:


l.to_csv("C:\\Users\\DELL\\Desktop\\Abhyaz_Task\\data uplode\\contact_list_final.csv", index=False, header=True)


# In[74]:


l['name_start'] = l['Company Name'].str[:5]
l['email_start'] = l['Email ID'].str[:5]
result = l[l['name_start'] == l['email_start']]


# In[40]:


#result
# Extract columns A, B, and C
all = l[['Company Name','Email ID','Company Type']]
o = result[['Company Name','Email ID','Company Type']]


# In[41]:


all


# In[42]:


o


# In[49]:


all.to_csv("C:\\Users\\DELL\\Desktop\\Abhyaz_Task\\data uplode\\contact_list_final.csv", index=False, header=True)


# In[ ]:




