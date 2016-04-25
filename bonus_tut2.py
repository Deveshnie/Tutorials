from numpy import sum,abs, concatenate,exp,pi,arange,complex
import numpy as np
def myfft(y):
    n=len(y)
   
    if n==1:
        return y
    else:
        a=y[0::3]
        b=y[1::3]
        c=y[2::3]
        j=complex(0,1)
        nn=n/3

        ftt1=myfft(a)+myfft(b)*exp(-2*pi*j*arange(0,nn)/n)+myfft(c)*exp(-4*pi*j*arange(0,nn)/n)
        ftt2=myfft(a)+myfft(b)*exp(-2*pi*j*arange(0,nn)/n)*exp(-2*pi*j/3)+myfft(c)*exp(-4*pi*j*arange(0,nn)/n)*exp(-4*pi*j/3)   
        ftt3=myfft(a)+myfft(b)*exp(-2*pi*j*arange(0,nn)/n)*exp(-4*pi*j/3)+myfft(c)*exp(-4*pi*j*arange(0,nn)/n)*exp(-2*pi*j/3) 
        y=np.concatenate((ftt1,ftt2,ftt3))
        return y
        
points=[3,9,27,81]
for i in points:
    y=np.random.randn(i)
    yft1=np.fft.fft(y)
    yft2=myfft(y)
    print sum(abs(yft1-yft2))