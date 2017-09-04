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
    if '*' in counts:
        counts['*'] = counts['*']+len(labels)
    else:
        counts['*'] = len(labels)
    
    for l in labels:
        key = l
        if key in counts:
            counts[key] = counts[key]+1
        else:
            counts[key] = 1
        
        if key+',*' in counts:
            counts[key+',*'] = counts[key+',*']+len(words)
        else:
            counts[key+',*'] = len(words)
        
        for w in words:
            longkey = key+','+w
            if longkey in counts:
                counts[longkey] = counts[longkey]+1
            else:
                counts[longkey] = 1
                      

def count(file):
    counts = {}
    total_labels = set()
    currentdoc = file.readline()
    
    while(currentdoc):   
        labels, words = extractinfo(currentdoc)
        
        total_labels = total_labels.union(set(labels))
        updatecount(labels,words,counts)
        
        currentdoc = file.readline()
    
    file.close()
    
    return list(total_labels),counts

if __name__ == '__main__':
    file = sys.stdin
    labels,counts = count(file)
    pickle.dump(labels,sys.stdout)
    pickle.dump(counts,sys.stdout)
    
        
    