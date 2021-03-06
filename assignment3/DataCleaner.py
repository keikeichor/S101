#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as sq


# In[2]:


mydb = sq.connect(host = "localhost",user = "root", password = "123456789!", buffered = True,
                 auth_plugin='mysql_native_password', allow_local_infile=True)


# In[3]:


mycursor = mydb.cursor()


# In[4]:


mycursor.execute("CREATE DATABASE NJ;")


# In[5]:


mycursor.execute("CREATE TABLE NJ.teacher (last_name VARCHAR(50), first_name VARCHAR(50),county VARCHAR(100),district VARCHAR(100), school VARCHAR(200), primary_job VARCHAR(300),fte DOUBLE, salary INT,certificate VARCHAR(100),subcategory VARCHAR(50), teaching_route VARCHAR(50),highly_qualified VARCHAR(200), experience_district INT,experience_nj INT,experience_total INT);")


# In[6]:


mycursor.execute("LOAD DATA LOCAL INFILE '/Users/kkc/Desktop/harvard/Python for Engineering/week2/nj_state_teachers_salaries.csv'                  INTO TABLE NJ.teacher                  FIELDS TERMINATED BY ','                  LINES TERMINATED BY '\n'                   IGNORE 1 ROWS;")


# In[7]:


mycursor.execute("SHOW TABLES FROM NJ;")


# In[8]:


for db in mycursor:
    print(db)


# In[9]:


mycursor.execute("USE NJ;")


# In[10]:


mycursor.execute("SELECT * FROM teacher;")


# In[11]:


for db in mycursor:
    print(db)


# In[ ]:





# ### Load csv data into Pandas DataFrame:

# In[12]:


import pandas as pd
import numpy as np


# In[13]:


teacher_df = pd.read_csv(r'nj_state_teachers_salaries.csv', low_memory=False) 
teacher_df.head(5)


# In[14]:


teacher_df.columns


# ###  <font color='green'> Comment: the column names are correct. </font>

# In[15]:


teacher_df.dtypes


# ###  <font color='green'> Comment: there are inconsistent data types in column #6, #12, #13, #14, and most values are identified as 'object' rather than string, integers and floats. </font>

# In[16]:


teacher_df.isna().sum()


# ###  <font color='green'> Comment: there are NaN values in almost every variable, and therefore need to be cleaned.</font>

# ###  <font color='green'> if we randomly select one variable, 'district' == NaN, we can see there are at least 9 entries: </font>

# In[17]:


teacher_df[teacher_df['district'].isna()]


# In[ ]:





# ###  <font color='green'> cleaning the data step1 - dropping the rows with at least one NaN values: </font>

# In[18]:


teacher_df_cleaned = teacher_df.dropna() 
teacher_df_cleaned.head(5)


# In[19]:


print( 'dropped', teacher_df.count().max() - teacher_df_cleaned.count()[1], 'rows with NaN values')


# In[20]:


print('total rows without NAN values are:', teacher_df_cleaned.count()[0])


# In[ ]:





# ###  <font color='green'> cleaning the data step2 - convert the string values with leading and tailing spaces trimmed: </font>

# In[21]:


pd.options.mode.chained_assignment = None 

str_list = ['last_name', 'first_name', 'county','district', 'school', 'primary_job',
           'certificate', 'subcategory', 'teaching_route', 'highly_qualified']

for i in str_list:
    teacher_df_cleaned[i] = teacher_df_cleaned[i].astype(pd.StringDtype())
    teacher_df_cleaned[i] = teacher_df_cleaned[i].str.strip()


# In[22]:


teacher_df_cleaned.head(5)


# In[23]:


teacher_df_cleaned.loc[teacher_df_cleaned['last_name'].str.strip().str[0]== ' ']


# In[24]:


teacher_df_cleaned.loc[teacher_df_cleaned['county'].str.strip().str[-1]== ' ']


# ###  <font color='green'> comment: the string values are successfully trimmed with leading and tailing spaces. </font>

# In[ ]:





# ###  <font color='green'> cleaning the data step3 - as the csv auto loading in python suggests columne'fte', 'experience_district','experience_nj' and 'experience_total' have inconsistent data types, we now check what will be the most appropriate data types for these variables: </font>

# In[ ]:





# ###  <font color='green'> step 3.1 - we first need to check if there's any strange, non-numeric values. We convert the numeric objects to float values as to be safe, some of the numeric variables are integers, but floats will include those. However, when converting the objects to floats, the errors should be 'coerce' then the non-numeric values will be replaced with NaN: </font>

# In[25]:


num_list = ['fte', 'experience_district', 'experience_nj', 'experience_total' ]

for n in num_list:
    teacher_df_cleaned[n] = pd.to_numeric(teacher_df_cleaned[n],errors = 'coerce')


# ###  <font color='green'> the new NaN values are those that contain non-numeric values, as shown below, there are 10 non-numeric values identified and marked as NaN. and we drop the NAs again to have the final clean data: </font>

# In[26]:


teacher_df_cleaned.isna().sum()


# In[27]:


teacher_df_cleaned = teacher_df_cleaned.dropna()


# In[28]:


teacher_df_cleaned.isna().sum()


# In[29]:


teacher_df_cleaned.count()


# In[30]:


print('final rows without NaNs and non-numeric values are:', teacher_df_cleaned.count()[0])


# In[ ]:





# In[31]:


teacher_df_cleaned.dtypes


# In[ ]:





# ###  <font color='green'> step 3.2 - if we want to be more specific whether the numeric values are integers or floats, we can first convert the float values into string, and strip out the last value to see if it is zero: </font>

# In[ ]:





# In[ ]:





# In[32]:


int_pd = pd.DataFrame()

int_check_list = ['fte','experience_district', 'experience_nj', 'experience_total']

for m in int_check_list:
    int_pd[m] = teacher_df_cleaned[m].astype(pd.StringDtype()).str.strip().str[-1]== '0' 


# ###  <font color='green'> combine the stripped-out values into a dataframe, 'True' means the last value is 0, so this is an integer, otherwise it is a float: </font>

# In[33]:


int_pd.tail(5)


# ###  <font color='green'> apparently there are non-zero values in this dataframe: </font>

# In[34]:


int_pd[(int_pd['experience_total']== False) | (int_pd['fte']== False) |  (int_pd['experience_district']== False)
      | (int_pd['experience_nj']== False) ]


# In[35]:


int_pd['fte'].unique()


# In[36]:


int_pd['experience_total'].unique()


# In[37]:


int_pd['experience_district'].unique()


# In[38]:


int_pd['experience_nj'].unique()


# ###  <font color='green'> Comments: so only 'fte' is a float type, the other three variables are integers. This also helps us cross-validate the SQL input when we create table. </font>

# In[ ]:





# In[39]:


teacher_df_cleaned.head(5)


# In[ ]:





# In[40]:


teacher_df_cleaned.to_csv('new_nj_state_teachers_salaries.csv', index= False)


# In[ ]:





# In[ ]:





# In[ ]:




