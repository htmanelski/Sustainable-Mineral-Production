# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:15:01 2021

@author: Henry Manelski
"""

import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd

# plotting for the SAG Mills 

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
plt.savefig('1.jpg',dpi=500)
plt.show()



# plotting for the Ball Mills

F_80 = np.linspace(50,2000,500)
P_80 = 10

W_i = 15
E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

plt.plot(F_80,E_G,label=r'$15$ (kWh/t)')

W_i = 20
E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

plt.plot(F_80,E_G,label=r'$20$ (kWh/t)')

W_i = 25
E_G = 10*W_i*((1/np.sqrt(P_80)-(1/np.sqrt(F_80))))

plt.plot(F_80,E_G,label=r'$25$ (kWh/t)')
plt.title(r'$E_G$ vs $P_{80}$ (Ball Mill, $P_{80}=10$ $\mu$m)')

plt.legend(title=r'$W_i$')
plt.xlabel(r'$F_{80}$ (microns)') 
plt.ylabel(r'$E_G$ (kWh/t)')
plt.savefig('2.jpg',dpi=500)
plt.show()
