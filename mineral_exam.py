# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:18:50 2021

@author: Henry Manelski
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'mineral_exam_1.csv', sep=',')

df['V(x)'] = (df['F(x)']*0.4/5.6)/0.678
df['Cumulative V(x)'] = np.cumsum(df['V(x)'])

# we need to remember to convert between microns and centimeters
df['N(x)'] = df['V(x)']/(4/3*np.pi*(df['x']/20000)**3)
df['Cumulative N(x)'] = np.cumsum(df['N(x)'])

df['A(x)'] = df['N(x)']*4*np.pi*(df['x']/20000)**2
df['Cumulative A(x)'] = np.cumsum(df['A(x)'])

plt.title('4.2')
plt.plot(df['x'],df['F(x)'])
plt.xlabel('x (microns)')
plt.ylabel('F(x)')
plt.xscale('log')
plt.show()

plt.title('4.3')
plt.plot(df['x'],df['F(x)'],label='F(x)')
plt.axhline(y=0.5, linestyle='dashed',label='P50',c='red')
plt.axhline(y=0.8, linestyle='dashed',label='P80',c='green')
plt.plot(df['x'],np.cumsum(df['F(x)']),label='Cumulative')
plt.xlabel('x (microns)')
plt.ylabel('Fraction Passing')
plt.legend()
plt.xscale('log')
plt.show()

#df.to_csv('')