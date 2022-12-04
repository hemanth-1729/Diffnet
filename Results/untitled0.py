#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 23:21:56 2021

@author: kongarahemanth
"""

import numpy as np

df=np.load("/Users/kongarahemanth/Documents/Academics/Advanced Deep Learning/Project3/data/yelp/user_vector.npy")

print(df.shape,df[::2])
