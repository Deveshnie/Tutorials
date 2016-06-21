# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:17:20 2016

@author: Deveshnie
"""

import numpy as np
def get_legendre(x,order):
    
    mat=np.zeros([x.size,order])
    mat[:,0]=1.0
    if order>1:
        mat[:,1]=x
    for i in range(1,order-1):
        mat[:,i+1]=((2.0*i+1)*x*mat[:,i]-i*mat[:,i-1])/(i+1.0)
    
    return np.matrix(mat)

if __name__=='__main__':
   
    x=np.arange(-1,1,0.01)

    for order in np.arange(1,11,1):
        mat=get_legendre(x,order)
        
        
    y=np.exp(get_legendre(x,10))
    A=(get_legendre(x,10))
    fitp=np.linalg.inv(A.transpose()*A)*A.transpose()*np.matrix(y)
    err=np.abs(np.mean(y))
    pred=A*fitp
    print err
    print fitp

       