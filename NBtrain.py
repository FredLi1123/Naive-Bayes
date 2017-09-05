#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:28:33 2017

@author: Nuoyu Li (nuoyul@andrew.cmu.edu)
"""

import sys
import helper
        
def extractinfo(document):
    # split a line to the string of labels and the document content
    parts = document.split('\t',1)
    
    # use helper functions to obtain the lists of labels and words
    labels = helper.get_labels(parts[0])
    words = helper.tokenizeDoc(parts[1])
    
    return labels, words

def updatecount(labels,words,counts):
    if '*' in counts:
        counts['*'] = counts['*']+len(labels)
    else:
        counts['*'] = len(labels)
    
    for l in labels:
        if l in counts:
            counts[l] = counts[l]+1
        else:
            counts[l] = 1
        
        if l+',*' in counts:
            counts[l+',*'] = counts[l+',*']+len(words)
        else:
            counts[l+',*'] = len(words)
        
        for w in words:
            longkey = l+','+w
            if longkey in counts:
                counts[longkey] = counts[longkey]+1
            else:
                counts[longkey] = 1
                      
def count(trainfile):
    counts = {}
    currentdoc = trainfile.readline()
    
    while currentdoc:   
        labels, words = extractinfo(currentdoc)
        updatecount(labels,words,counts)
        currentdoc = trainfile.readline()
    
    trainfile.close()
    
    return counts

def writecount(counts):
    countstr = ''
    
    for key in counts:
        countstr += (key+'\t'+str(counts[key])+'\n')
    sys.stdout.write(countstr)
    

if __name__ == '__main__':
    trainfile = sys.stdin
    counts = count(trainfile)
    writecount(counts)
    
    
    
        
    