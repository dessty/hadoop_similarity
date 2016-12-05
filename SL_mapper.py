# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 21:00:07 2016

@author: Moehu
"""

#!/usr/bin/env python
import sys
import pandas as pd
import numpy as np
import csv

key=[]
value=[]
data=[]

#for line in sys.stdin:
with open("ratings.csv") as csvfile:
    reader = csv.reader(csvfile)
    firsline = True
    for line in reader:
        if firsline:
            firsline = False
            continue
        if key != line[0] or key == None:
            if value:
                # print"%s %s\n"%(key, value)
                data.append([key, value])
            key = line[0]
            value = {}
            value.update({line[1]:line[2]})
        else:
            value.update({line[1]:line[2]})

result= pd.DataFrame(data)

userid=list(set(result[0]))
userid.sort()


value_=[]
mapper=[]
for k in range(3):
    for j in range(k+1,len(userid)):
         key_=userid[k],userid[j]
         a=list(result.loc[result[0] == userid[k],][1])
         a=dict(a[0])
         b=list(result.loc[result[0] == userid[j],][1])
         b=dict(b[0])
         intersect = set(a.keys()).intersection(b.keys())
         intersect = list(intersect)
         if len(intersect) == 0:
             value_ = 999
         else:
             value_=[[a[x] for x in intersect],[b[x] for x in intersect]]
         #print('{0}\t{1}'.format(key_ ,value_) )
         #print('\t')
         print([key_,value_])
