import numpy as np
class NbodyStarter:
    def __init__(self,N=5):
        self.m=np.empty(N)  #make N empty places in array
        self.m.fill(5)      #fill in empty spaces with 5
        self.x=np.random.randn(N)  #fill in N random numbers  
        self.y=np.random.randn(N)
        self.vy=np.zeros_like(N)
        self.vx=np.zeros_like(N)
        self.options={}
        self.options['G']= 6.67e-11
        self.options['N']=N
   
    def __GravPot2__(self):
        
        potential=np.zeros(self.options['N'])
    
        for i in range(0,self.options['N']):
            for j in range(i+1,self.options['N']): 
                xx=self.x[i]-self.x[j]#finding distances between particles
                yy=self.y[i]-self.y[j]
                radius=np.sqrt(xx**2+yy**2) #make sure distance between particles is poitive
                potential[i]=potential[i]+self.m[i]*self.m[j]*self.options['G']*1.0/radius
        return potential  
        
    def __GravPot__(self):
        
        potential=np.zeros(self.options['N'])
      
        for i in range(0,self.options['N']): 
            for j in range(0,self.options['N']):
                if (i!=j):
                    xx=self.x[i]-self.x[j] #finding distances between particles
                    yy=self.y[i]-self.y[j]
                    radius=np.sqrt(xx**2+yy**2) #make sure distance between particles is poitive             
                    potential[i]=potential[i]+self.m[i]*self.m[j]*self.options['G']*1.0/radius
        return potential  
              
Nclass=NbodyStarter()
print Nclass.__GravPot2__().sum()
print (Nclass.__GravPot__().sum())*0.5
        