#!/usr/bin/env python
# coding: utf-8

# Code modified version of https://www.tensorflow.org/tutorials/load_data/pandas_dataframe
# Code works with PyCharm View --> Scientific mode or Jupyter.

# In[1]:


from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import tensorflow as tf


# In[2]:


csv_file = tf.keras.utils.get_file('train_ssh_events.csv', 'https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_events.csv')


# In[3]:


df = pd.read_csv(csv_file)


# In[4]:


df.head()


# In[5]:


df.dtypes


# In[ ]:




