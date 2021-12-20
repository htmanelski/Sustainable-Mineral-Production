"""
Final Project
EAEE 4200
Mission Mine Flow Sheet

Tkinter and Python

Henry Manelski and David Tibbits
December 2021
"""

#Importation of important modules (Directly from MinLab0.0.2)
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 
import random
import os
import glob

#Get Current directory, set as cd.
cd = os.getcwd()

#establish root for tkinter
root = Tk()
root.geometry("1440x900")
root.title('Mission Mine Flow Sheet V.1.0')

#Creates background image
img = ImageTk.PhotoImage(Image.open(cd + "/Background.png"))
background = Label(root, image = img)
background.place(relx=0.5, rely=0.5, anchor='center')  

#creates foreground frame
foreground = Frame(root).place(x=0, y=0)

#creates taskbar frame on sie of foreground
Taskbar = Frame(foreground).place(x=1100, y=0)

#functions
def update():
    global feed_var
    global OF1_var
    global OF2_var
    global SAG_out
    global Dis1_label
    global Dis2_label
    global Dis3_label
    global OF1_label
    global OF2_label
    global Cir1_label
    global Cir2_label
    
    Feed = int(feed_var.get())
    Ratio1 = float(OF1_var.get())
    Ratio2=float(OF2_var.get())
    
    #SAG Mill Output
    SAG_out= Feed/2 + (1-Ratio1)*Feed/Ratio1/2
    
    Circulating = (1-Ratio1)*Feed/Ratio1
    
    Ball_out= Feed + (1-Ratio2)*Feed/Ratio2
    
    Circulating2 = (1-Ratio2)*Feed/Ratio2
    
    Dis1_label.place_forget()
    Dis2_label.place_forget()
    Dis3_label.place_forget()
    OF1_label.place_forget()
    OF2_label.place_forget()
    Cir1_label.place_forget()
    Cir2_label.place_forget()
    
    Dis1_label = Label(foreground, text= "Mill Discharge: " + str(SAG_out)[0:4]+ " t/hr")
    Dis2_label = Label(foreground, text= "Mill Discharge: " + str(SAG_out)[0:4]+ " t/hr")
    Dis3_label = Label(foreground, text= "Mill Discharge: " + str(Ball_out)[0:4]+ " t/hr")
    OF1_label = Label(foreground, text= "Overflow: " + str(Feed) + " t/hr")
    OF2_label = Label(foreground, text= "Overflow: " + str(Feed) + " t/hr")
    
    Cir1_label = Label(foreground, text= "Circulating load: " + str(Circulating)[0:4] + " t/hr")
    Cir2_label = Label(foreground, text="Circulating load: " + str(Circulating2)[0:4] + " t/hr")
    
    Dis1_label.place(x=280, y=580)
    Dis2_label.place(x=280, y=775)
    Dis3_label.place(x=700, y=440)
    OF1_label.place(x=560, y=480)
    OF2_label.place(x=880, y=430)
    Cir1_label.place(x=120 , y=790)
    Cir2_label.place(x=680 , y=600)
    pass

def Cycl1():
    global cy1_sheet
    global df_1
    global P50_1
    global P80_1
    global graph1_label
    global Cir1_label
    global Cir2_label
    
    cy1_sheet = filedialog.askopenfilename(title="Open a Spreadsheet", initialdir=cd)
    
    df_1 = pd.read_csv(cy1_sheet)

    df_1['V(x)'] = (df_1['F(x)']*0.4/5.6)/0.678
    df_1['Cumulative V(x)'] = np.cumsum(df_1['V(x)'])

    P50_1 = float(df_1.iloc[(np.cumsum(df_1['F(x)'])-0.5).abs().argsort()[:1]]['x'])
    P80_1 = float(df_1.iloc[(np.cumsum(df_1['F(x)'])-0.8).abs().argsort()[:1]]['x'])
    
    F_80 = 150000
    P_80 = np.linspace(10000,500,500)

    W_i = 15
    E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

    plt.plot(P_80,E_G,label=r'$15$ (kWh/t)')

    W_i = 20
    E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

    plt.plot(P_80,E_G,label=r'$20$ (kWh/t)')

    W_i = 25
    E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

    plt.plot(P_80,E_G,label=r'$25$ (kWh/t)')
    plt.title(r'$E_G$ vs $P_{80}$ (SAG Mill, $F_{80}=1.5$ cm)')

    plt.legend(title=r'$W_i$')
    plt.xlabel(r'$P_{80}$ (microns)') 
    plt.ylabel(r'$E_G$ (kWh/t)')
    plt.savefig('1.jpg',dpi=50)

    g1 = ImageTk.PhotoImage(Image.open("1.jpg"))
    graph1_label = Label(foreground, image=g1).place(x=1100, y=100)
    graph1_label.g1 = g1
    
    plt.close()
    
    pass

def Cycl2():
    global cy2_sheet
    global df_2
    global P50_2
    global P80_2
    global wi_var
    
    cy2_sheet = filedialog.askopenfilename(title="Open a Spreadsheet", initialdir=cd)
    
    df_2 = pd.read_csv(cy1_sheet)

    df_2['V(x)'] = (df_2['F(x)']*0.4/5.6)/0.678
    df_2['Cumulative V(x)'] = np.cumsum(df_2['V(x)'])

    P50_2 = float(df_1.iloc[(np.cumsum(df_2['F(x)'])-0.5).abs().argsort()[:1]]['x'])
    P80_2 = float(df_1.iloc[(np.cumsum(df_2['F(x)'])-0.8).abs().argsort()[:1]]['x'])

    F_80 = np.linspace(P80_2,2000,500)
    P_80 = P80_2

    W_i = 15
    E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

    plt.plot(F_80,E_G,label=r'$15$ (kWh/t)')

    W_i = int(wi_var.get())
    E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

    plt.plot(F_80,E_G,label=str(wi_var.get()) + '(kWh/t)')

    W_i = 25
    E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

    plt.plot(F_80,E_G,label=r'$25$ (kWh/t)')
    plt.title(r'$E_G$ vs $P_{80}$ (Ball Mill, $P_{80}$ $\mu$m)')

    plt.legend(title=r'$W_i$')
    plt.xlabel(r'$F_{80}$ (microns)') 
    plt.ylabel(r'$E_G$ (kWh/t)')
    plt.savefig('2.jpg',dpi=50)
    
    image = Image.open(cd + "/2.jpg")
    image.resize((300, 200), Image.ANTIALIAS)
    
    g2 = ImageTk.PhotoImage(image)
    graph2_label = Label(foreground, image=g2).place(x=1100, y=300)

    plt.close()

#create widgets

#creates labels in foreground
headframe_label = Label(foreground, text = "Mission Mine Feed")
crusher_label = Label(foreground, text = "Primary Crusher")
SAG1_label = Label(foreground, text = "SAG Mill #1")
SAG2_label = Label(foreground, text = "SAG Mill #2")
Cyclone1_label = Label(foreground, text = "Hydrocyclone #1")
Cyclone2_label = Label(foreground, text = "Hydrocyclone #2")
Ball_label = Label(foreground, text = "Ball Mill")
Cir1_label = Label(foreground, text = "Circulating Load")
Cir2_label = Label(foreground, text = "Circulating Load")
Float_label = Label(foreground, text = "Flotation Systems")
Thick_label = Label(foreground, text = "Concentrate Thickening")
Filt_label = Label(foreground, text = "Concentrate Pressure Filtration")
Conc_label = Label(foreground, text = "Copper Concentrate")
ASARCO_label = Label(foreground, text = "To ASARCO Smelter")
Hayden_label = Label(foreground, text = "in Hayden, AZ")

feed_label = Label(foreground, text= "Feed Rate (t/hr):")
wi_label = Label(foreground, text="Bond's Work Index:")

Dis1_label = Label(foreground, text= "")
Dis2_label = Label(foreground, text= "")
Dis3_label = Label(foreground, text= "")
OF1_label = Label(foreground, text= "")
OF2_label = Label(foreground, text= "")

ratio1_label = Label(foreground, text= "O/F Ratio:")
ratio2_label = Label(foreground, text= "O/F Ratio:")


#creates text variables for spin boxes in foreground
feed_var = StringVar(value=0)
wi_var = StringVar(value=0)
OF1_var = StringVar(value=0)
OF2_var = StringVar(value=0)

#creates spin boxes in foreground
feed_box = Spinbox(foreground,from_=0, to=10000, textvariable=feed_var, command=update)
wi_box = Spinbox(foreground,from_=0, to=10000, textvariable=wi_var, command=update)
OF1_box = Spinbox(foreground,from_=0, to=1, textvariable=OF1_var, increment=0.1, width=5,  command=update)
OF2_box = Spinbox(foreground,from_=0, to=1, textvariable=OF2_var, increment=0.1, width=5, command=update)

#place labels in foreground
headframe_label.place(x=40 , y=115)
crusher_label.place(x=70 , y=320)
SAG1_label.place(x=285 , y=435)
SAG2_label.place(x=285 , y=640)
Cyclone1_label.place(x=520 , y=700)
Cyclone2_label.place(x=940 , y=600)
Ball_label.place(x=730 , y=435)
Cir1_label.place(x=150 , y=790)
Cir2_label.place(x=680 , y=600)
Float_label.place(x=940 , y=100)
Thick_label.place(x=620 ,y=85)
Filt_label.place(x=620 ,y=140)
Conc_label.place(x=540 ,y=295)
ASARCO_label.place(x=320, y=220)
Hayden_label.place(x=330 ,y=240)

feed_label.place(x=175, y=30)
wi_label.place(x=175, y=80)

ratio1_label.place(x=480, y=525)
ratio2_label.place(x=880, y=437)

#places spin boxes in foreground
feed_box.place(x=175, y=50)
wi_box.place(x=175, y=100)
OF1_box.place(x=480 ,y=545 )
OF2_box.place(x=880 ,y=457 )


#creates labels in taskbar 
Cycl1_label = Label(Taskbar, text="Select Distribution for Cyclone #1")
Cycl2_label = Label(Taskbar, text="Select Distribution for Cyclone #2")

#places labels
Cycl1_label.place(x=1100, y=30)
Cycl2_label.place(x=1100, y=60)

#creates buttons
Cyc1_but = Button(Taskbar, text="Browse", command=Cycl1)
Cyc2_but = Button(Taskbar, text="Browse", command=Cycl2)

#places buttons
Cyc1_but.place(x=1330, y=30)
Cyc2_but.place(x=1330, y=60)

#establishes the mainloop of the tkinter root
root.mainloop()
