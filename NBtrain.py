#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:28:33 2017

@author: Nuoyu Li (nuoyul@andrew.cmu.edu)
"""

import sys
import pickle
import helper
        
def extractinfo(document):
    parts = document.split('\t',1)
    labels = helper.get_labels(parts[0])
    words = helper.tokenizeDoc(parts[1])
    
    return labels, words

def updatecount(labels,words,counts):
    if 'y=*' in counts:
        counts['y=*'] = counts['y=*']+len(labels)
    else:
        counts['y=*'] = len(labels)
    
    for l in labels:
        key = 'y='+l
        if key in counts:
            counts[key] = counts[key]+1
        else:
            counts[key] = 1
        
        if key+',w=*' in counts:
            counts[key+',w=*'] = counts[key+',w=*']+len(words)
        else:
            counts[key+',w=*'] = len(words)
        
        for w in words:
            longkey = key+',w='+w
            if longkey in counts:
                counts[longkey] = counts[longkey]+1
            else:
                counts[longkey] = 1
                      

def count(file):
    counts = {}
    currentdoc = file.readline()
    
    while(currentdoc):   
        labels, words = extractinfo(currentdoc)
        updatecount(labels,words,counts)
        
        currentdoc = file.readline()
    
    file.close()
    
    return counts

if __name__ == '__main__':
    file = sys.stdin
    counts = count(file)
    pickle.dump(counts,sys.stdout.buffer)
    
    
        
    