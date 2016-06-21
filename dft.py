# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:51:06 2016

@author: Deveshnie
"""

import matplotlib.pyplot as plt
import numpy as np

def exponential(y,k):
    j=np.complex(0,1)
    num=2*np.pi*j*k*y/y.size
    exp=np.exp(num)
    return exp.sum()
def fn(y):
    x=np.exp(-0.5*(y)**2/0.3**2)
    return x
    
y=np.arange(-10,10,1.0)
x=np.exp(-0.5*(y)**2/0.3**2)
k=4
f=exponential(x,k)*fn(y).sum()
print f
