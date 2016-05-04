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

    '''        
    def __GravitationalPotential__(self):
        potential=np.zeros(self.options['N'])
        
        for i in range(0,self.options['N']):
            for j in range(0,self.options['N']):
                #radius=np.sqrt(((self.x[i,:]-self.y[j,:])**2).sum())
                radius=np.sqrt(((self.x[i,:]-self.y[j,:])**2).sum())
                if (i!=j):
                    #potential[i]=potential[i]-m[i]*m[j]*self.options['G']/radius
                    potential[i]=self.m[i]*self.m[j]*self.options['G']*1.0/radius
        return potential.sum()    
    '''
    def __GravPot__(self):
        
        potential=np.zeros(self.options['N'])
        
       # for i in range(0,self.options['N']):
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                x=self.x[i]-self.x[j]#finding distances between particles
                y=self.y[i]-self.y[j]
                radius=np.sqrt(x**2+y**2) #make sure distance between particles is poitive
                if (i!=j):
                    potential[i]=self.m[i]*self.m[j]*self.options['G']*1.0/radius
        return 0.5*potential.sum()    
        

    def __GravPot2__(self):
        
        potential=np.zeros(self.options['N'])
        
       # for i in range(0,self.options['N']):
        for i in range(len(self.m)):
            for j in range(i+1,len(self.m)):
                x=self.x[i]-self.x[j]#finding distances between particles
                y=self.y[i]-self.y[j]
                radius=np.sqrt(x**2+y**2) #make sure distance between particles is poitive
                potential[i]=self.m[i]*self.m[j]*self.options['G']*1.0/radius
        return potential.sum()   
        
Nclass=NbodyStarter()
print Nclass.__GravPot2__()
print Nclass.__GravPot__()
        