# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 21:00:07 2016

@author: Moehu
"""

#!/usr/bin/env python
import sys
import pandas as pd
import csv


key=[]
value=[]
data=[]
firsline = True

for line in sys.stdin:
    line = line.split(",")
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
         key_=userid[k] + ',' + userid[j]
         a=list(result.loc[result[0] == userid[k],][1])
         a=dict(a[0])
         b=list(result.loc[result[0] == userid[j],][1])
         b=dict(b[0])
         intersect = set(a.keys()).intersection(b.keys())
         intersect = list(intersect)
         if len(intersect) == 0:
             value_ = '999_999'
         else:
             value_a= [a[x] for x in intersect]
             value_b= [b[x] for x in intersect]
             value_= str(value_a).strip("[]") + '_' + str(value_b).strip('[]')

            #  value_= value_a + '_' + value_b

         #print('{0}\t{1}'.format(key_ ,value_) )
         #print('\t')
         print '%s_%s'%(key_,str(value_).replace("'", "").replace(" ", ""))
