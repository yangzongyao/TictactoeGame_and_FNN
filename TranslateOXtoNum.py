#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 00:23:02 2019

@author: yang
"""
import numpy as np

def transateOX(d):
    d = np.array(d, dtype='<U2') #unicode, if <U1 -1 can't show
    d = d.reshape(9)
    
    for i in range(len(d)):
        if d[i] == 'O':
            d[i] = 1
        elif d[i] == 'X':
            d[i] = -1.0
        else:
            d[i] = 0
    d = d.astype(int)
    return d