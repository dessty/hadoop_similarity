# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 21:16:31 2016

@author: Moehu
"""

#!/usr/bin/env python
import sys
import numpy as np
import math

print '\\**************************\n*\tREDCUCER\n**************************\\'
for input_line in sys.stdin:
    print input_line
    print input_line[0]
    exit()
    key = input_line[0]
    value = input_line[1]
    if value == 999:
        print(key)
    else:
        S=len(value[0])
        a1=np.array(value[0])
        a2=np.array(value[1])
        b1=a1.astype(np.float)
        b2=a2.astype(np.float)
        Dist= sum(b1-b2)**2/S
        print( "{0}\t{1}".format(key, Dist))
