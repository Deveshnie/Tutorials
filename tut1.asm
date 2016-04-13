1) ls -lrt #displays last file in directory first.
2) sed -n '16,25p' nameOfFile.fileExtension #eg. sed -n '16,25p' hello_world.py
	or
   head -16 nameOfFile #the name of the file must have the file extension included eg. head -16 hello_world.py
3) man Python (Displays python commands)

4)
import numpy as np # imports numpy
input('enter a value for n', n)
z=np.linspace(0.0,np.pi/2,n, endpoint=True) # displays an array of n  vectors including the endpoint pi/2 (the value 
												of n can be inputted)
print z #prints the array

5)
import numpy as np
z=[ 10,30,100,300,1000,3000]  			#determines the number of evenly spaced numbers between 0 and pi/2 
										over which the function is integrated
x0=0									#initial value
xn=np.pi/2								#final value 
for dx in z:							#loops over the z values (first the integral is evaluated over 10 evenly spaced
										numbers, then over 30 etc.)
    x=(np.linspace(x0,xn,dx))			#vector of evenly spaced numbers is created and stored in x
    y=np.cos(x)							
    total=y.sum()*(x[1]-x[0])
    print 'integral is '+repr(total)+' and dx is '+repr(dx)
    

The error becomes smaller when more points are taken between 0 and pi/2. The error in this case is given by 
E_r=(f'(c)/2)(b-a)^2. The integral evaluated over 10 points is '1.0847266943914424'. It is '1.0268381925388663'
over 30 points, '1.0079123355326245' over 100 points, '1.0026244497712877' over 300 points, and '1.0007859783191271'
over 1000 points.
6)
x[1::2] #all odd points from array
x[2:-1:2] #all even points from array skipping first and last points




