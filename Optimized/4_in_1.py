#importing modules to main_code
import FileDialog 
import matplotlib.pyplot as plt
from functions.function import *
from matplotlib.widgets import Slider,Button  # import the Slider widget
import matplotlib.ticker as ticker
from matplotlib.ticker import NullFormatter, FixedLocator
import numpy as np


print("Welcome !!!")
#print("Enter all the values in the MKS system")

global Phi_m,tox,NA,ND,r,count,Qox,Qc


#user input
#NA=float(input("Enter the value of NA in per m^3 :"))
#tox=float(input("Enter the value of oxide thickness in nm :"))
#Phi_m=float(input("Enter the value of Phi_m :"))


#constants initialize
q=1.6*10**(-19)	        
Eo=8.854*10**(-12)	
ks=11.7			#ks for Si
kox=3.9			#kox for SiO2
Ni=1.15*10**16		
Phi_t=0.0259            #Thermal Voltage Phi_t=k*t/q

tox=2*10**(-9)
#tox=tox*10**(-9)
NA=5*10**23
Phi_m=0.56
ND=0
Qox=10**(-5)


#variable declaration
r=[]	
Y_list={}
V_list={}
Y1_list={}
V1_list={}
Y2_list={}
V2_list={}
Y3_list={}
V3_list={}
Cox_list={}
Cox_val_list={}

count=0
Y_list[count]=[]
V_list[count]=[]
Y1_list[count]=[]
V1_list[count]=[]
Y2_list[count]=[]
V2_list[count]=[]
Y3_list[count]=[]
V3_list[count]=[]
Cox_list[count]=[]
Cox_val_list[count]=[]

graph_plot={}
graph_plot1={}
graph_plot2={}
graph_plot3={}
graph_plot4={}

Es=ks*Eo		
Eox=kox*Eo		

colour_count=1
colours={1:'b',2:'g',3:'r',4:'c',5:'m',6:'y',7:'k'}



plt.title="Different graphs"
# plotting_graph
fig,((ax1, ax2), (ax3, ax4))= plt.subplots(2,2,sharey=False)
plt.subplots_adjust(left=0.05, bottom=0.30,right=0.95,top=0.95)

mu, sigma = 1e-3, 1e-4
#s = np.random.normal(mu, sigma, 10000)


#1
ax1.set_xlim(-1,2) 
ax1.set_ylim(0,1.3) 

ax1.set_xlabel('Vgb (in V)') 
ax1.set_ylabel('SHI_S (in V)')
#2
ax2.set_xlabel('SHI_S (in V)') 
ax2.set_ylabel('Q (in C/m^2)')


ax2.set_xlim(0,1.5) 
ax2.set_ylim(0,15*10**(-3)) 
#ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%1.2E'))


#3
ax3.set_xlim(-1,2) 
ax3.set_ylim(0,0.03) 

ax3.set_xlabel('Vgb (in V)') 
ax3.set_ylabel('Q (in C/m^2)')
#4
ax4.set_xlim(-1,1.5) 
ax4.set_ylim(0,0.03) 

ax4.set_xlabel('Vgb (in V)') 
ax4.set_ylabel('dQ/dVgb (in F/m^2)')


#2-D variable of graph
graph_plot[count]=[]
graph_plot[count],= plt.plot(V_list[count], Y_list[count],color ='r',label="")	

graph_plot1[count]=[]
graph_plot1[count],= plt.plot(V1_list[count], Y1_list[count],color ='r',label="")	

graph_plot2[count]=[]
graph_plot2[count],= plt.plot(V2_list[count], Y2_list[count],color ='r',label="")	

graph_plot3[count]=[]
graph_plot3[count],= plt.plot(V3_list[count], Y3_list[count],color ='r',label="")	

graph_plot4[count]=[]
graph_plot4[count],= plt.plot(Cox_list[count], Cox_val_list[count],color ='r',label="")	


plt.legend()



#initial text
#txt= plt.text(-0.2, -0.2, 'Sliders', fontsize=18)		#xloc,yloc,txt,fontsize


#button function for adding plots
def setValue(val):
	global count,colour_count,colours,Qox
	count=count+1
	print("count is ",count)
	
	Y_list[count]=[]
	V_list[count]=[]
	graph_plot[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	graph_plot1[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	graph_plot2[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	graph_plot3[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]
	graph_plot4[count]=[]
	
	r=[]
	Po=NA	
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Cox=Eox/tox	
	Vfb=-Phi_m-Shi_F-Qox/Cox	#ignoring the potential drop across the oxide layer
	gm=(sqrt(2*q*Es*NA))/(Cox)
	
	for i in drange(-0.5,1.5,0.05):
		r.append(i)
	
	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
		x0= min(f,n)	
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No))
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po)
		print("the der val is : ",dq_dVgb)
		
		V_list[count].append(Vgb)
		Y_list[count].append(val)

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc))

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc))

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb)

		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox)

	colour_count=colour_count+1
	
	plt.axes(ax1)	
	graph_plot[count],= plt.plot(V_list[count], Y_list[count],color =colours[colour_count],label="Curve "+str(count))			
	plt.legend()

	plt.axes(ax2)
	graph_plot1[count],= plt.plot(V1_list[count], Y1_list[count],color =colours[colour_count],label="Curve "+str(count))			
	plt.legend()


	plt.axes(ax3)	
	graph_plot2[count],= plt.plot(V2_list[count], Y2_list[count],color =colours[colour_count],label="Curve "+str(count))			
	plt.legend()

	plt.axes(ax4)	
	graph_plot3[count],= plt.plot(V3_list[count], Y3_list[count],color =colours[colour_count],label="Curve "+str(count))
	graph_plot4[count],= plt.plot(Cox_list[count], Cox_val_list[count],color =colours[colour_count],linestyle='--')
			
	plt.legend()


	#txt.remove()	
	#txt= plt.text(-0.3, -0.15, 'Slider '+str(count), fontsize=18)	#xloc,yloc,txt,fontsize
	




#sliders Update functions of Tox
def val_update_tox(val):
    global tox,NA,Phi_m,count,Qox
	
    if count!=0:
	r=[]
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	tox=slider1.val
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Cox=Eox/tox			
	Vfb=-Phi_m-Shi_F-Qox/Cox
	gm=(sqrt(2*q*Es*NA))/(Cox)

	for i in drange(Vfb+0.01,1.5,0.05):
		r.append(i)

   	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No))
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po)		
		V_list[count].append(Vgb)
		Y_list[count].append(val)

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc))

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc))

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb)
		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox)
	print("Cox is ",Cox)
	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	
	plt.draw          # redraw the plot



#sliders Update functions of NA
def val_update_NA(val):
    global tox,NA,Phi_m,count,Qox

    if count!=0:
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	r=[]
	NA=(slider2.val)*10**23
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6		
	Cox=Eox/tox
	Vfb=-Phi_m-Shi_F-Qox/Cox
	gm=(sqrt(2*q*Es*NA))/(Cox)
   	
	for i in drange(Vfb+0.01,1.5,0.05):
		r.append(i)

	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No))
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po) 
		V_list[count].append(Vgb)
		Y_list[count].append(val)

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc))

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc))

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb)
		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox)

	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	plt.draw          # redraw the plot


#sliders Update functions of Phi_m
def val_update_Phi(val):
    global tox,NA,Phi_m,count,Qox

    if count!=0:
	print("Count inside Phi_m is ",count)
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	r=[]
	Phi_m=slider3.val
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6		
	Cox=Eox/tox
	Vfb=-Phi_m-Shi_F-Qox/Cox
	gm=(sqrt(2*q*Es*NA))/(Cox)
   	
	for i in drange(Vfb+0.01,1.5,0.05):
		r.append(i)

	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No)) 
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po)
		V_list[count].append(Vgb)
		Y_list[count].append(val)

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc))

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc))

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb)
		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox)

	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	plt.draw          # redraw the plot



#sliders Update functions of Qox
def val_update_Qox(val):
    global tox,NA,Phi_m,count,Qox

    if count!=0:
	print("Count inside Phi_m is ",count)
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	r=[]
	Qox=(slider4.val)*10**(-6)
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6		
	Cox=Eox/tox
	print("Cox is ",Qox/Cox)
	Vfb=-Phi_m-Shi_F-Qox/Cox
	gm=(sqrt(2*q*Es*NA))/(Cox)
   	
	for i in drange(Vfb+0.01,1.5,0.05):
		r.append(i)

	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No)) 
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po)
		V_list[count].append(Vgb)
		Y_list[count].append(val)

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc))

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc))

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb)
		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox)

	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	plt.draw          # redraw the plot


#button_declaration
axButton = plt.axes([0.83,0.10, 0.06, 0.06])		#xloc,yloc,width,heights
btn = Button(axButton, ' ADD ')
	

#button on click callback function
btn.on_clicked(setValue)


#Sliders declaration
axSlider1= plt.axes([0.1,0.20,0.55,0.02])		#xloc,yloc,width,height
slider1 = Slider(ax=axSlider1,label='Tox',valmin=1*10**(-9),valmax=5*10**(-9),valinit=tox,valfmt='tox is '+'%1.11f'+ ' in m',color="green")


axSlider2= plt.axes([0.1,0.15,0.55,0.02])		#xloc,yloc,width,height
slider2 = Slider(axSlider2,'NA', valmin=1, valmax=20,valinit=NA/(10**23),valfmt='NA is '+'%1.2f'+ ' in 10**23 m^-3')


axSlider3= plt.axes([0.1,0.10,0.55,0.02])		#xloc,yloc,width,height
slider3 = Slider(axSlider3,'Phi_m', valmin=0.01, valmax=2,valinit=Phi_m,valfmt='Phi_m is '+'%1.2f',color="red")


axSlider4= plt.axes([0.1,0.05,0.55,0.02])		#xloc,yloc,width,height
slider4 = Slider(axSlider4,'Qox', valmin=0.01, valmax=100,valinit=Qox*10**6,valfmt='Qox is '+'%1.2f'+'*10^(-6)',color="yellow")


#sliders on change function call
slider1.on_changed(val_update_tox)
slider2.on_changed(val_update_NA)
slider3.on_changed(val_update_Phi)
slider4.on_changed(val_update_Qox)

plt.show()


print("Thank you for using the tool \n")
