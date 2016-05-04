import numpy as np
class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def copy(self):
        return Complex(self.r,self.i)
    def __sub__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r-val.r
            ans.i=ans.i-val.i
        else:
            try: 
                ans.r=ans.r-val
            except:
                print 'Invalid type in Complex.__sub__'
                ans=None
        return ans
    def __mul__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
        
            r1=ans.r*val.r
            r2=-ans.i*val.i
            i1=self.i*val.r+self.r*val.i
            ans=Complex(r1+r2,i1)
        else:
            try:
                ans=Complex(ans.r*val,ans.i)
            except:
                print 'Invalid type in Complex.__mul__'
                ans=None
        return ans
    def __div__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            #numerator
            ans.r1=(ans.r)*(val.r)
            ans.i1=(-ans.i)*(-val.i)
            ans.i2=ans.i*val.r+ans.r*(-val.i)
            denominator=val.r**2+val.i**2

            #ans=self*val*(1.0/denominator)
            ans=Complex(ans.r1*(1.0/denominator)+ans.i1*(1.0/denominator),ans.i2*(1.0/denominator))#*(1.0/denominator)
        else:
            try:
                ans=Complex(ans.r*(1.0/val),ans.i*(1.0/val))
            except:
                print 'Invalid type in Complex.__div__'
                ans=None
        return ans
   
   
    def __complicatedPower__(self,power):
        ans=self.copy()
        theta=np.arctan(self.i,self.r)
        
        ans=((self.i**2+self.r**2)**power*(1.0/2))*np.exp(power.i*(theta))  
        return ans
    def __repr__(self):
        if (self.i<0):
            return repr(self.r)+' - '+repr(-1*self.i) +'i'
        else:
            return repr(self.r)+' + '+repr(self.i) +'i'

if __name__=='__main__':
    print '__sub__'
    a=Complex(2,5)
    b=Complex(4,-3)
    f=2
    c=a-b
    g=a-b-f
    print g
    print c
    d=a-b-2
    print d
    l='a'
    m=c-l
    print m
    
    print
    print 'multiply'
    print  
    a=Complex(2,5)
    b=Complex(4,-3)
    c=a*b
    print c
    d=a*2
    print d
    
    print 
    print 'division'
    print
    a=Complex(3,2)
    b=Complex(4,-3)
    c=a/b
    print c
    c=a/2
    print c
    print
    print 'power'
    I=complex(0,1)
    a=2*I
    print a**2
    print (2+4*I)**(3*5*I)
    print a**2.4