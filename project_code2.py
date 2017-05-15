# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:06:08 2017

@author: Jack
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []
dict = {}
number = 0

def graph(x,y):
    x2 = np.arange(len(x))    
    plt.bar(x2,y)
    plt.xticks(x2, x, rotation= 'vertical')
    plt.title('video games with sales greater than 100,000 copies')
    plt.xlabel('Genres')
    plt.ylabel('Sales in North America (in millions)')
    plt.show()
    
    
with open('vgsales2.csv','r') as f:
    reader = csv.reader(f, delimiter = ',')
    next(reader)
    
    for row in reader:
        x.append(row[4])
        y.append(float(row[6]))
        number += 1   
        if(number == 11):
            break
        
        
print()       
print()     
print(x)
print() 
print(y)
print()

graph(x,y)