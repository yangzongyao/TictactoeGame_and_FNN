# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 23:35:21 2018

@author: 19point
"""

def Computer(desktop):
    i = [[100,50,100],
         [50,200,50],
         [100,50,100]]
    
    best_location_num = -1
    best_location_x = -1
    best_location_y = -1
        
    for a in range(3):
        if desktop[a][0] == desktop[a][1] and desktop[a][0] != 0:
            if desktop[a][0] == 'X':
                i[a][2] = 500
            elif desktop[a][0] == 'O':
                i[a][2] = 1000
        elif desktop[a][0] == desktop[a][2] and desktop[a][0] != 0:
            if desktop[a][0] == 'X':
                i[a][1] = 500
            elif desktop[a][0] == 'O':
                i[a][1] = 1000
        elif desktop[a][2] == desktop[a][1] and desktop[a][1] != 0:
            if desktop[a][1] == 'X':
                i[a][0] = 500
            elif desktop[a][1] == 'O':
                i[a][0] = 1000
        for b in range(3):
            if desktop[0][b] == desktop[1][b] and desktop[0][b] != 0:
                if desktop[0][b] == 'X':
                    i[2][b] = 500
                elif desktop[0][b] == 'O':
                    i[2][b] = 1000
            elif desktop[0][b] == desktop[2][b] and desktop[0][b] != 0:
                if desktop[0][b] == 'X':
                    i[1][b] = 500
                elif desktop[0][b] == 'O':
                    i[1][b] = 1000
            elif desktop[1][b] == desktop[2][b] and desktop[1][b] != 0:
                if desktop[1][b] == 'X':
                    i[0][b] = 500
                elif desktop[1][b] == 'O':
                    i[0][b] = 1000
            if desktop[a][b] != 'O' and desktop[a][b] != 'X':
                if i[a][b] >= best_location_num:
                    best_location_num = i[a][b]
                    best_location_x = a
                    best_location_y = b
    
    
    #print(best_location_x,',',best_location_y)
    return best_location_x+1,best_location_y+1