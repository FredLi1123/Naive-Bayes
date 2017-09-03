#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:28:33 2017

@author: Nuoyu Li (nuoyul@andrew.cmu.edu)
"""

import sys

def readcommandline():
    try:
        inputfile = open(sys.argv[1],'r')
        return inputfile
    except Exception as e:
        print('invalid file directory, try again')
        print('usage: python NBtrain.py <inputfile>')
        sys.exit(2)

if __name__ == '__main__':
    openfile = readcommandline()
    for line in openfile:
        print(line.strip())
        
    