#!/usr/bin/env python
# coding: utf-8

# # MDS Central Limit Theorem Homework

# ### Question 1 - Experiment to sample from a normal distribution

# In[ ]:


import numpy as np # this package contains important numerical handling functions
from scipy import stats # this package is used for scientific and technical computing -- this is an example of importing just one part of a larger package.
import matplotlib.pyplot as plt # this package is used for creating static, animated, and interactive visualizations in Python. 
# feel free to use other packages, like seaborn, etc.


# In[ ]:


def sample_normal_distribution(mean, std_dev, n):
    """
    Returns the mean value observed from n samples taken from a normal distribution
    """
    samples = np.random.normal(mean, std_dev, n)
    sample_mean = np.mean(samples)
    return sample_mean


# In[ ]:


# Here is the specific computational experiment for a range of different n and 
# enough trials to understand the long-range behavior of sampling

n = range(1,50)
num_trials = 1000
mu = 3
std_dev = 1

sample_dict = {}
for i in n:
    means = []
    for _ in range(num_trials):
        sample_mean = sample_normal_distribution(mu, std_dev, i)
        means.append(sample_mean)
    sample_dict[i] = means

# Check this shape makes sense
print(f"Number of different n values: {len(sample_dict.keys())}")
print(f"Number of trials for each n: {len(sample_dict[1])}")

