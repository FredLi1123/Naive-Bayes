#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:15:51 2017

@author: Nuoyu Li (nuoyul@andrew.cmu.edu)
"""

import sys
import math
import helper

def readcounts():
    labels = []
    counts = {}
    words = set()
    
    line = sys.stdin.readline()
    while line:
        entry = line.split('\t')
        key = entry[0]
        count = entry[1]
        
        counts[key] = int(count)
        
        if ',' not in key and key != '*': 
            labels.append(key)
        elif ',' in key:
            word = key.split(',')[1]
            if word != '*':
                words.add(word)
        
        line = sys.stdin.readline()      
    
    return len(words),labels,counts
            
def readcommandline(): 
    try: 
        inputtestfile = open(sys.argv[1],'r') 
        return inputtestfile 
    except Exception: 
        print('invalid testfile directory, try again') 
        print('usage: python NBtrain.py <testfile>') 
        sys.exit(2)

def extractinfo(document):
    parts = document.split('\t',1)
    labels = parts[0].split(',')
    words = helper.tokenizeDoc(parts[1])
    
    return labels, words

def test(testfile,V,labels,counts):
    currentdoc = testfile.readline()
    diml = len(labels)
    
    correctdocs = 0
    totaldocs = 0
    
    while(currentdoc):
        current_labels, words = extractinfo(currentdoc)
        
        maxprob = float('nan')
        testlabel = ''
        
        for l in labels:
            prior = math.log(counts[l]+1)-math.log(counts['*']+diml)
            posterior = 0
            
            for w in words:
                if l+','+w in counts:
                    posterior = posterior+math.log(
                            counts[l+','+w]+1)-math.log(counts[l+',*']+V)
                else:
                     posterior = posterior-math.log(counts[l+',*']+V) 
            
            maxprob = max(prior+posterior,maxprob)
            if maxprob == prior+posterior: testlabel = l
        
        print(str(current_labels)+'\t'
              +str(testlabel)+'\t'
                  +"{0:.4f}".format(maxprob))
       
        if testlabel in current_labels: correctdocs += 1
        totaldocs += 1
        
        currentdoc = testfile.readline()
    
    testfile.close()
    print('Percent correct:\t'+
          str(correctdocs)+'/'+str(totaldocs)+'='+
             "{0:.4f}".format(correctdocs/totaldocs))

if __name__ == '__main__':
    V,labels,counts = readcounts()
    testfile = readcommandline()
    test(testfile,V,labels,counts)