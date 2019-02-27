# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 23:59:13 2018

@author: 19point
"""

import os,desk,WinLose
import Computer
import TranslateOXtoNum as tonum

def play():
    deskTop = [[0,0,0],
               [0,0,0],
               [0,0,0]]
    mod = 'X'
    data = 'start,'
    while True:
        try:
            print('Player ',mod,' : ')
            if mod == 'X':
                i, j = map(int,input('Enter location : ').split(' '))
            elif mod == 'O':
                i, j = Computer.Computer(deskTop)
            if i > 3 or j > 3 or i == 0 or j == 0:
                if i == 0 and j == 0:
                    os.system('clear')
                    break
            elif deskTop[i-1][j-1] != 0:
                print('This location is write already.')
                continue
            print('Enter error.')
        except ValueError as n:
            print(n)
        except IndexError as n:
            print(n)
        else:
            os.system('clear')
            deskTop[i-1][j-1] = mod
            desk.desk(deskTop)
            d = deskTop
            d = tonum.transateOX(d)
            if mod == 'X':
                f = open('TrainingSet.txt', 'a')
                for i in d:
                    data += str(i) + ','
                data += '\n'
                f.write(data)
                data = 'data,'
                mod = 'O'
            elif mod == 'O':
                f = open('TrainingSet.txt', 'a')
                for i in d:
                    data += str(i) + ','
                data += '\n'
                f.write(data)
                data = 'label,'
                mod = 'X'
            if WinLose.CheckWinner(deskTop) == 'Over':
                a = input('Enter any key to exit.')
                os.system('clear')
                break;
                