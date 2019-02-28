#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 00:13:45 2019

@author: yang
"""


def dataOperator():
    f = open('TrainingSet.txt', 'r')
    data = f.readlines()
    dataSplit = []
    traindata = []
    trainlabel = []
    for i in data:
        dataSplit.append(i.split(','))
    for i in dataSplit:
        if i[0] == 'data':
            traindata.append(i[1:10])
        elif i[0] == 'label':
            trainlabel.append(i[1:10])
        elif i[0] == 'start':
            trainlabel.append(i[1:10])
            traindata.append(['0','0','0','0','0','0','0','0','0'])
    return traindata, trainlabel

        
d, l = dataOperator()