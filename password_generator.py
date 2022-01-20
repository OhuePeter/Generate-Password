#!/usr/bin/env python
# coding: utf-8

# # Generate single password

# In[16]:


import random

def password(length):
    psw = str()
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for i in range(length):
        psw = psw + random.choice(char)
        return psw
password(8)


# # Generate multiple password

# In[18]:


import string
from random import *
char = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(char) for x in range(randint(12, 20)))
print(password)


# In[ ]:




