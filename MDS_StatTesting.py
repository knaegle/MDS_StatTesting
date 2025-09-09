#!/usr/bin/env python
# coding: utf-8

# # MDS Statistical Testing Homework

# ## Question 1 - Experiment to test differential expression

# In[1]:


import numpy as np # this package contains important numerical handling functions
from scipy import stats # this package is used for scientific and technical computing -- this is an example of importing just one part of a larger package.
import matplotlib.pyplot as plt # this package is used for creating static, animated, and interactive visualizations in Python. 
# feel free to use other packages, like seaborn, etc.


# In[2]:


# Here is the specific computational experiment that gets samples from an underlying distribution and compares them

n = 3
num_trials = 100

alpha = 0.05

mu_1 = 1
sigma_1 = 1
mu_2 = 3
sigma_2 = 1

# Example of doing a t-test on one pair of samples of size n, sampled from two different distributions
samples_1 = np.random.normal(mu_1, sigma_1, n)
samples_2 = np.random.normal(mu_2, sigma_2, n)

# Compare the two samples
t_stat, p_value = stats.ttest_ind(samples_1, samples_2)

print("p_value: %.3e" % p_value)
if p_value < alpha:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


# ## Question 2: Multiple hypothesis correction

# In[3]:


import MHC

alpha = 0.05


# In[ ]:


# The pvalue array from the FDR paper to use for testing
p_val_array = [0.0095, 0.0201, 0.0278, 0.0298, 0.0344, 0.0001, 0.0004, 0.0019, 1.0, 0.759, 0.6528, 0.5719, 0.4262, 0.3240, 0.0459]

bonferroni_alpha = MHC.bonferroni(p_val_array, alpha)
print("Corrected alpha (Bonferroni): %.3e" % bonferroni_alpha)
print("Number of rejections (Bonferroni): %d" % sum(p < bonferroni_alpha for p in p_val_array))

