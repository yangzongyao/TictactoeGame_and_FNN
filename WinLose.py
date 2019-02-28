# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 21:07:50 2018

@author: 19point
"""

def CheckWinner(i):
    if i[0][0] == i[0][1] == i[0][2] and i[0][0] != 0:
        print('Player',i[0][0],'is Winner!')
        return 'Over'
    elif i[1][0] == i[1][1] == i[1][2] and i[1][0] != 0:
        print('Player',i[1][0],'is Winner!')
        return 'Over'
    elif i[2][0] == i[2][1] == i[2][2] and i[2][0] != 0:
        print('Player',i[2][0],'is Winner!')
        return 'Over'
    elif i[0][0] == i[1][0] == i[2][0] and i[0][0] != 0:
        print('Player',i[0][0],'is Winner!')
        return 'Over'
    elif i[0][1] == i[1][1] == i[2][1] and i[0][1] != 0:
        print('Player',i[0][1],'is Winner!')
        return 'Over'
    elif i[0][2] == i[1][2] == i[2][2] and i[0][2] != 0:
        print('Player',i[0][2],'is Winner!')
        return 'Over'
    elif i[0][0] == i[1][1] == i[2][2] and i[0][0] != 0:
        print('Player',i[0][0],'is Winner!')
        return 'Over'
    elif i[0][2] == i[1][1] == i[2][0] and i[0][2] != 0:
        print('Player',i[0][2],'is Winner!')
        return 'Over'
    else:
        num = 0
        for a in range(3):
            for b in range(3):
                if i[a][b] != 0:
                    num += 1
        if num == 9:
            print('No one win.')
            return 'Over'
        return 'Continue'
"""
CheckWinner([['O','O','X'],
             ['X','X','O'],
             ['O','X','X']])
"""