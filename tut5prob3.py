import numpy
import numpy as np
from matplotlib import pylab as plt
def simulate_gaussian(t,sig=0.5,amp=1,cent=0):
    dat=numpy.exp(-0.5*(t-cent)**2/sig**2)*amp
    dat+=numpy.random.randn(t.size)
    return dat

def sim_lorentzian(t,a=1.0,b=1.0,c=1.0):
    dat=a/(b+(t-c)**2)
    dat+=numpy.random.randn(t.size)
    return dat  

def get_trial_offset(sigs):
    return sigs*numpy.random.randn(sigs.size)

class Gaussian:
    def __init__(self,t,sig=0.5,amp=1.0,cent=0,offset=0):
        self.t=t
        self.y=simulate_gaussian(t,sig,amp,cent)+offset
        self.err=numpy.ones(t.size)
        self.sig=sig
        self.amp=amp
        self.cent=cent
        self.offset=offset

    def get_chisq(self,vec):
        sig=vec[0]
        amp=vec[1]
        cent=vec[2]
        off=vec[3]

        pred=off+amp*numpy.exp(-0.5*(self.t-cent)**2/sig**2)
        chisq=numpy.sum(  (self.y-pred)**2/self.err**2)
        return chisq
class Lorentzian:
    
    def __init__(self,t,a=1.0,b=1.0,c=1.0,offset=0):
        self.t=t
        self.y=sim_lorentzian(t,a,b,c)+offset
        self.a=a
        self.err=np.ones(t.size)
        self.b=b
        self.c=c
        self.offset=offset
        
    def get_chisq(self,vec):
        a=vec[0]
        b=vec[1]
        c=vec[2]   
        
        off=vec[3]
        
        pred=off+a/(b+(self.t-c)**2)
        chisq=numpy.sum(  (self.y-pred)**2/self.err**2)
        return chisq
        
def run_mcmc(data,start_pos,nstep,scale=None):
    nparam=start_pos.size
    params=numpy.zeros([nstep,nparam+1])
    params[0,0:-1]=start_pos
    cur_chisq=data.get_chisq(start_pos)
    cur_pos=start_pos.copy()
    if scale==None:
        scale=numpy.ones(nparam)
    for i in range(1,nstep):
        new_pos=cur_pos+get_trial_offset(scale)
        new_chisq=data.get_chisq(new_pos)
        if new_chisq<cur_chisq:
            accept=True
        else:
            delt=new_chisq-cur_chisq
            prob=numpy.exp(-0.5*delt)
            if numpy.random.randn()<prob:
                accept=True
            else:
                accept=False
        if accept: 
            cur_pos=new_pos
            cur_chisq=new_chisq
        params[i,0:-1]=cur_pos
        params[i,-1]=cur_chisq
    return params


if __name__=='__main__':
    
   
    t=numpy.arange(-5.0,5.0,0.01)
  
    dat=Lorentzian(t,b=2.5)


    guess=numpy.array([0.4,1.0,0.4,0.2])
    scale=numpy.array([0.01,0.01,0.01,0.01])
    nstep=100000
    chain=run_mcmc(dat,guess,nstep,scale)
    nn=numpy.round(0.2*nstep)
    chain=chain[nn:,:]
    
   
    param_true=numpy.array([dat.a,dat.b,dat.c,dat.offset])
    for i in range(0,param_true.size):
        val=numpy.mean(chain[:,i])
        scat=numpy.std(chain[:,i])
        print [param_true[i],val,scat]
