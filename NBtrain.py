#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:28:33 2017

@author: Nuoyu Li (nuoyul@andrew.cmu.edu)
"""

import sys
import re
import helper

def readcommandline():
    try:
        inputfile = open(sys.argv[1],'r')
        return inputfile
    except Exception as e:
        print('invalid file directory, try again')
        print('usage: python NBTrain.py <inputfile>')
        sys.exit(2)
        
def extractinfo(document):
    parts = document.split('\t',1)
    labels = helper.get_labels(parts[0])
    words = helper.tokenizeDoc(parts[1])
    
    return labels, words

def updatecount(labels,words,counts):
    

def train(filestream):
    counts = {}
    currentdoc = filestream.readline()
    
    while(currentdoc):   
    

if __name__ == '__main__':
    
    
        
    