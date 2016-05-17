import numpy as np

def trig(n,val):
    k=2*np.pi*np.arange(0,n)/n      #2*pi*xi/N
    rowval=val*2-1
    A=np.zeros([n,rowval])
    A[:,0]=1.0
    j=1
    count=1
    while (j<rowval):
        A[:,int(j)]=np.cos(k*count)
        A[:,int(j+1)]=np.sin(k*count)*(-1)
        j+=2
        count+=1
    a=np.matrix(A)  
    return a

n=1000
val=7
x_expect=np.random.randn(n)
x=np.matrix(x_expect).transpose()
A=trig(n,val)

xft=np.fft.fft(x_expect)
#m=(A^TA)^{-1}*(A^Td)
lhs=A.transpose()*A
rhs=A.transpose()*x
m=np.linalg.inv(lhs)*(rhs)
I=np.complex(0,1)
err_4=m[7]+I*m[8]-xft[4]*2/n
print 'error in 4th term is ',err_4

