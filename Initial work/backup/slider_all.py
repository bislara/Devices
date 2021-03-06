#importing modules to main_code
import matplotlib.pyplot as plt
from functions.function import *
from matplotlib.widgets import Slider  # import the Slider widget


print("Welcome !!!")
print("Enter all the values in the MKS system")

global Phi_m,tox,NA,ND,Condition,r


#user input
NA=float(input("Enter the value of NA in per m^3 :"))
tox=float(input("Enter the value of oxide thickness in nm :"))
Phi_m=float(input("Enter the value of Phi_m :"))



#constants initialize
q=1.6*10**(-19)	        
Eo=8.854*10**(-12)	
ks=11.7			#ks for Si
kox=3.9			#kox for SiO2
Ni=1.15*10**16		
Phi_t=0.0259            #Thermal Voltage Phi_t=k*t/q



#variable declaration
r=[]	
Y_list=[]
V_list=[]

#tox=2*10**(-9)
tox=tox*10**(-9)
#NA=5*10**23
#Phi_m=0.56
ND=0

Es=ks*Eo		
Eox=kox*Eo		



#initial calculations for first graph
#to take 0.1 steps in Vgb
for i in range(-4,15):
	r.append(i/10.0)

for Vgb in r:
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F			#ignoring the potential drop across the oxide layer
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
	f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
	x0= min(f,n)	
	val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
	#print("the val is : ",val)
	Y_list.append(val)
	V_list.append(Vgb)



# plotting_graph

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)

plt.ylim(0,1.2) 
plt.xlim(-1,2) 

plt.title('Vgb VS SHI graph') 
plt.legend()

plt.xlabel('Vgb value') 
plt.ylabel('SHI value')

#2-D variable of graph
graph_plot,= plt.plot(V_list, Y_list,color ='r',label="tox=2nm")	
plt.legend()




#Sliders declaration
axSlider1= plt.axes([0.1,0.16,0.6,0.03])
slider1 = Slider(ax=axSlider1,label='Tox',valmin=1*10**(-9),valmax=5*10**(-9),valinit=tox,valfmt='tox is '+'%1.11f'+ ' in m',color="green")

plt.title('Sliders')

axSlider2= plt.axes([0.1,0.10,0.6,0.03])
slider2 = Slider(axSlider2,'NA', valmin=1, valmax=20,valinit=NA/(10**23),valfmt='NA is '+'%1.2f'+ ' in 10**23 m^-3')


axSlider3= plt.axes([0.1,0.05,0.6,0.03])
slider3 = Slider(axSlider3,'Phi_m', valmin=0.01, valmax=2,valinit=Phi_m,valfmt='Phi_m is '+'%1.2f',color="red")




#sliders Update functions
def val_update_tox(val):
	global tox,NA
	r=[]
	Y_list=[]
	V_list=[]
	tox=slider1.val
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F
	Cox=Eox/tox		
	gm=(sqrt(2*q*Es*NA))/(Cox)

	for i in range(Vfb*10+1,20):
		r.append(i/10.0)

   	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		Y_list.append(val)
		V_list.append(Vgb)

	graph_plot.set_ydata(Y_list)
	graph_plot.set_xdata(V_list)
	plt.draw          # redraw the plot


def val_update_NA(val):
	global tox,NA,Phi_m
	Y_list=[]
	V_list=[]
	r=[]
	NA=(slider2.val)*10**23
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
   	
	for i in range(Vfb*10+1,20):
		r.append(i/10.0)

	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		Y_list.append(val)
		V_list.append(Vgb)
	
	graph_plot.set_ydata(Y_list)
	graph_plot.set_xdata(V_list)
	plt.draw          # redraw the plot


def val_update_Phi(val):
	global tox,NA,Phi_m
	Y_list=[]
	V_list=[]
	r=[]
	Phi_m=slider3.val
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
   	
	for i in range(Vfb*10+1,20):
		r.append(i/10.0)

	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		Y_list.append(val)
		V_list.append(Vgb)
	
	graph_plot.set_ydata(Y_list)
	graph_plot.set_xdata(V_list)
	plt.draw          # redraw the plot



#sliders on change function call
slider1.on_changed(val_update_tox)
slider2.on_changed(val_update_NA)
slider3.on_changed(val_update_Phi)


plt.show()

