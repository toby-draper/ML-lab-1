# %% [markdown]
# ## Step One
# ### College Completion
# This dataset contains information on the success and progress of college students in America. One question it could be used to address is comparing graduation rates between ethnicities.

# ### Job Placement
# This dataset contains information on former students and factors about their work experience. One question it could be used to address is comparing the salaries of male and female students in the same major.
# %% [markdown]
# ## Step Two: 
# ### Problem Definition:
# College Completion: What are the differences in graduation rates between HBCUs and non-HBCUs?
# - Independent Business Metric: HBCU
# 
# Job Placement: What are the differences in salaries across men and women of the same major?
# - Independent Business Metric: Gender
# 
# ### Data Preparation Steps:
# See below:
# %%
# import packages
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import MinMaxScaler, StandardScaler 

# set variables for dfs
college_completion = pd.read_csv("data/cc_institution_details.csv")
job_placement = pd.read_csv("data/Placement_Data_Full_Class 2.csv")

# %%
# examine college completion:
college_completion.info()

# %%
# drop unneeded columns
to_keep = [8,13,30,32]
college_completion_new = college_completion[college_completion.columns[to_keep]]

college_completion_new.info()
# %%
# transform hbcu values into binary using one hot encoding
college_completion_encoded = pd.get_dummies(college_completion_new, columns=['hbcu'])
college_completion_encoded["hbcu_X"] = (college_completion_encoded["hbcu_X"].astype(int))

college_completion_encoded.info()
college_completion_encoded.head()

# %%
# normalize continuous variables
# because graduation rate is a percentage, we don't need to scale it

# %%
# calculate hbcu prevalence
# %%
# examine job placement:
job_placement.info()
