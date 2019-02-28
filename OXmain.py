# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:31:42 2018

@author: 19point
"""

import Twoplayer as tp
import Oneplayer as op
import desk,os

while True:
    print('Welcome to play OX game.')
    print()
    print('+--------------------+')
    print('+ 1.Two players      +')
    print('+ 2.One player       +')
    print('+--------------------+')

    enter = input('Select mod : ')

    if enter == '1':
        os.system('clear')
        desk.desk([[0,0,0],[0,0,0],[0,0,0]])
        tp.play()
        break;
    elif enter == '2':
        os.system('clear')
        desk.desk([[0,0,0],[0,0,0],[0,0,0]])
        op.play()
        break;
    else:
        break;