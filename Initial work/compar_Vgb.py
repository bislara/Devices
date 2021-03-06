import matplotlib.pyplot as plt
from math import *
from sympy import *
import csv

global Y,deriv,dydx,count
count=0
h=5
global Vgb,Vfb,q,Es,Cox,Po,No,St,NA,ND


#intial values 
x0=0
Vgb=-1
Vfb=-1
NA=0
ND=0
St=0.0259
q=1.6*10**(-19)
#Es=1.05*10**(-10)
Es=11.7*8.854*10**(-12)

kox=3.9
Eo=8.854*10**(-12)
Eox=kox*Eo
tox=2.5*10**(-9)

Ni=1.18*10**16
#Cox=1.668*10**(-2)


#ni=1.26*10**13=sqrt(No*Po)
#PHI(f)=0.59266= PHI(t)*ln(NA/ni)
#2*PHI(f)= 1.1852

Y_list=[]
V_list=[]

i=0
r=[]

#Vfb=PHI(ms) + Q'o/C'ox

#funct to return the value of funct at a particuar value
def func(Vgb, Y ): 
    global Vfb,q,Es,Cox,Po,No,St,NA,ND
    #print("I am inside func  " , Y)
    try: 
      	  p=Vfb + Y + (sqrt(2*q*Es)/(Cox)) *(sqrt( Po*St*( e**(-Y/St )-1) +( NA-ND  )*Y + No*St*( e**(Y/St )-1) )  ) -Vgb
	  #print("the value of p is ",p)      	
	  return p 
    except ZeroDivisionError:
          print("Error!!!!!!!!!!!", Y)
    	  return 0    

#funct to find derivative in a particular value
def derivFunc( Y ): 
    k= deriv.doit().subs({t:Y})
   # print("I am inside deriv func  ", k)
    if k==0:
	return 1
    else:  
	return k

  
# Function to find the root 
def newtonRaphson( Vgb, Y ): 
    global count
    global Vfb,q,Es,Cox,Po,No,St,NA,ND,h
    if derivFunc(Y)!=0:
    	h = (func(Vgb,Y) )/ (derivFunc(Y)) 
    	print("h is ",h)

    while abs(h) >= 0.001: 
        count=count+1
	try:
      	    h = func(Vgb,Y)/derivFunc(Y)
	    Y = Y - h    
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", Y)
        # x(i+1) = x(i) - f(x) / f'(x) 
         
      
    #print("The value of the root is : ", 
     #                        "%.4f"% Y)
    print("the no of iterations is ",count)
    count=0 
    return Y


for i in range(0,150):
	r.append(i/100.0)

#loop for newton Raphson method and using diff intial value for diff Vgb
for Vgb in r:
	NA=5*10**23
	No=(Ni**2)/NA
	Po=NA
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
	f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
	n=0.826+0.026*6
	x0= min(f,n)
	print("Cox value is ",Cox)	
	t= Symbol('t')    
	f=Vfb + t + (sqrt(2*q*Es)/(Cox)) *(sqrt( Po*St*( e**(-t/St )-1) +( NA-ND  )*t + No*St*( e**(t/St )-1) )  ) -Vgb
	deriv= Derivative(f, t)
	val=newtonRaphson(Vgb,x0)  
	#print("the val is : ",val)
	Y_list.append(val)
	V_list.append(Vgb)

x2 = []
y2 = []

with open('Dataset/Final_Dataset.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append(row[0])
        y2.append(row[1])


# plotting_graph
plt.ylim(0.6,1.2) 
plt.xlim(0,1.5) 

plt.plot(V_list, Y_list,color ='r',label="NA=5*10^23")

plt.plot(x2,y2,color ='b', label='from excel!')





plt.xlabel('Vgb value') 
plt.ylabel('SHI value')

# show a legend on the plot 
plt.legend() 

plt.title('Vgb VS SHI graph') 
  
plt.show()   

