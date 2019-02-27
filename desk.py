# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 15:30:26 2018

@author: 19point
"""
def desk(i):
    print('       |       |       ')
    print('   ',end='')
    if(i[0][0] == 'O'):
        print('O',end='')
    elif(i[0][0] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   |   ',end='')
    if(i[0][1] == 'O'):
        print('O',end='')
    elif(i[0][1] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   |   ',end='')
    if(i[0][2] == 'O'):
        print('O',end='')
    elif(i[0][2] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   ')
    print('       |       |       ')
    print('-------|-------|-------')
    print('       |       |       ')
    print('   ',end='')
    if(i[1][0] == 'O'):
        print('O',end='')
    elif(i[1][0] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   |   ',end='')
    if(i[1][1] == 'O'):
        print('O',end='')
    elif(i[1][1] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   |   ',end='')
    if(i[1][2] == 'O'):
        print('O',end='')
    elif(i[1][2] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   ')
    print('       |       |       ')
    print('-------|-------|-------')
    print('       |       |       ')
    print('   ',end='')
    if(i[2][0] == 'O'):
        print('O',end='')
    elif(i[2][0] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   |   ',end='')
    if(i[2][1] == 'O'):
        print('O',end='')
    elif(i[2][1] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   |   ',end='')
    if(i[2][2] == 'O'):
        print('O',end='')
    elif(i[2][2] == 'X'):
        print('X',end='')
    else:
        print(' ',end='')
    print('   ')
    print('       |       |       ')