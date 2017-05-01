# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:27:53 2017

tutorial 2.2 from http://www.dyinglovegrape.com/data_analysis/part2/2da2.php

@author: Otto
"""

import pandas as pd
import numpy as np
#mit from braucht man nicht immer pd davor zu setzen..
from pandas import Series, DataFrame 

data2 = Series([8, 9, 11], index=["Joe", "Jane", "John"])

#mehrere JOes in einer mehreren index listen gibt probleme bei Pandas
data3 = Series([9,10,11], index=["Joe", "Joe", "John"])
#print(data3["Joe"])
data2 += 1

#print(data2 > 10) #falsch

print (data2[data2 >10]) #sehr geil

# np.random.rand(20) is an array of 20 random numbers

data4 = Series(np.random.rand(20))


print(len(data4[data4 <=0.75]))

"""
DataFrame is simple: in a Series, you construct one index for 
your elements; in a DataFrame, you construct two.
Usually, these two indices are represented 
by "column headers" and "row labels". 
"""
data = {'school': ['Baxters', 'Racine'],'test scores': [90, 96]}
table = DataFrame(data, index =['School 1', 'School 2'])
#print (table)

data = {'name' : ['James', 'Jane', 'John', 'Jake','Audrey'],
    'sex' : ['M', 'F', 'M', 'M', 'F'], 
    'age':[16,17,18,20,15], 
    'height':[77, 56, 66, 61, 50]}
#sort the colomns
table = DataFrame(data, columns=['name', 'age', 'sex', 'height']) 
print(table[['name', 'age']])

print(table.mean()) #anscheinend alles mit (nur) zahlen
print(table['age'].mean()) #so bekommt man nur den spezifischen wert


