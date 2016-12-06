# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 21:16:31 2016

@author: Moehu
"""

#!/usr/bin/env python
import sys
import numpy as np
import math
import csv
import operator
#

for line in sys.stdin:
    key,score1,score2 = line.strip().split('_')
    if (score1 == '999'):
        value = None
    else:
        s1=score1.split(',')
        s1=[float(i) for i in s1]
        s2=score2.split(',')
        s2=[float(i) for i in s2]
        S=len(score1)
        ab=map(operator.sub, s1, s2)
        ab=map(lambda x: x ** 2, ab)
        value= sum(ab)/S
    print( "{0}\t{1}".format(key,value))
