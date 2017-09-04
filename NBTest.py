#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:15:51 2017

@author: Nuoyu Li (nuoyul@andrew.cmu.edu)
"""

from __future__ import division
import sys
import math
import pickle
import helper

def readcommandline(): 
    try: 
        inputfile = open(sys.argv[1],'r') 
        return inputfile 
    except Exception as e: 
        print('invalid file directory, try again') 
        print('usage: python NBtrain.py <inputfile>') 
        sys.exit(2)

def extractinfo(document):
    parts = document.split('\t',1)
    labels = parts[0].split(',')
    words = helper.tokenizeDoc(parts[1])
    
    return labels, words

def test(file,labels,counts):
    currentdoc = file.readline()
    diml = len(labels)
    
    correctdocs = 0
    totaldocs = 0
    
    while(currentdoc):
        current_labels, words = extractinfo(currentdoc)
        dimw = len(words)
        
        maxprob = float('nan')
        testlabel = ''
        
        for l in labels:
            prior = math.log(counts[l]+1)-math.log(counts['*']+diml)
            posterior = 0
            
            for w in words:
                if l+','+w in counts.keys():
                    posterior = posterior+math.log(
                        counts[l+','+w]+1)-math.log(counts[l+',*']+dimw)
                else:
                     posterior = posterior-math.log(counts[l+',*']+dimw)  
            
            maxprob = max(prior+posterior,maxprob)
            if maxprob == prior+posterior: testlabel = l
        
        print(str(current_labels)+'\t'
              +str(testlabel)+'\t'
                  +str(round(maxprob,4)))
       
        if testlabel in current_labels: correctdocs += 1
        totaldocs += 1
        
        currentdoc = file.readline()
    
    file.close()
    print('Percent correct:\t'+
          str(correctdocs)+'/'+str(totaldocs)+'='+
             str(round(correctdocs/totaldocs,4)))

if __name__ == '__main__':
    labels = pickle.load(sys.stdin)
    counts = pickle.load(sys.stdin)
    file = readcommandline()
    test(file,labels,counts)