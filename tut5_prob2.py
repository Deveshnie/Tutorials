import numpy
from matplotlib import pylab as plt
def simulate_gaussian(t,sig=0.5,amp=1,cent=0):
    dat=numpy.exp(-0.5*(t-cent)**2/sig**2)*amp
    dat+=numpy.random.randn(t.size)
    return dat
    
def get_trial_offset(sigs):					#scale steps
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

def run_mcmc(data,start_pos,nstep,scale=None):
    nparam=start_pos.size					#assigns no of parameters based on no of items in guess
    params=numpy.zeros([nstep,nparam+1])	#records guess of parameter for each step
    params[0,0:-1]=start_pos				# first guess for the set of parameters in first row
    cur_chisq=data.get_chisq(start_pos)		#sets chisqu of current guess
    cur_pos=start_pos.copy()				#set current position to the initial guess
    counter1=0.0
    counter2=0.0
    if scale==None:
        scale=numpy.ones(nparam)			#stepsize scale=[1,1,1,1]
    for i in range(1,nstep):
        new_pos=cur_pos+get_trial_offset(scale)	#moves once from current position to a new guess
        new_chisq=data.get_chisq(new_pos)		#checks chisq of new guess
        if new_chisq<cur_chisq:
            accept=True						#accept new guess
        else:
            delt=new_chisq-cur_chisq
            prob=numpy.exp(-0.5*delt)			#
            if numpy.random.rand()<prob:		#if its within the noise of current step, accept guess, remember, random(betwn 0,1)
                accept=True
            else:
                accept=False
                counter2+=1
        if accept: 
            counter1+=1
            cur_pos=new_pos
            cur_chisq=new_chisq
        params[i,0:-1]=cur_pos			#[i,0] [i,1] [i,2] [i,3] [0:-1]=range(0 to 1 before last value (-1 in this case))
        params[i,-1]=cur_chisq			#putting chi squared in 5th (last) column
    count=counter1/float(nstep-1)
    return params,count


if __name__=='__main__':
    

    t=numpy.arange(-5,5,0.01)
    dat=Gaussian(t,amp=2.5)			#gaussian you wanted data for has amp=2.5


    guess=numpy.array([0.3,1.2,0.3,-0.2])    
   
    scale=numpy.array([0.1,0.1,0.1,0.1])		#0.1 stepsize
    
    #short chain first

    nstep=2000
    
    par_chain,countshortchain=run_mcmc(dat,guess,nstep,scale)		#chain is record of guesses and chisq, or params
    print 'for the short chain, the accept fraction is ',countshortchain
    nn=numpy.round(0.2*nstep)		
    par_chain=par_chain[int(nn):,:]			               
    
    newchain=par_chain[0:nstep,0:4]
    newscale=numpy.std(newchain,0) #we want to compute standard deviation of the 
                                    #parameters down the columns. axis=0
    nstep=40000          #get longer chain
    
    
    par_chain,countlongchain=run_mcmc(dat,par_chain[int(nn),0:4],nstep,newscale)
    print 'for the long chain we have accept fraction, ',countlongchain
   
    

    param_true=numpy.array([dat.sig,dat.amp,dat.cent,dat.offset])
    for i in range(0,param_true.size):
        val=numpy.mean(par_chain[:,i])			
											#find mean of that specific parameter, eg sig
        scat=numpy.std(par_chain[:,i])			#same thing with std dev
        print [param_true[i],val,scat]		#you check if the true param values are close to the mean and if the 
											#std dev values are small
        
