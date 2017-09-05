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
    total_labels = set()
    total_words = set()
    currentdoc = trainfile.readline()
    
    while(currentdoc):   
        labels, words = extractinfo(currentdoc)
        total_labels = total_labels.union(set(labels))
        total_words = total_words.union(set(words))
        updatecount(labels,words,counts)
        
        currentdoc = trainfile.readline()
    
    trainfile.close()
    
    return len(total_words),list(total_labels),counts

if __name__ == '__main__':
    trainfile = sys.stdin
    V,labels,counts = count(trainfile)
    pickle.dump(V,sys.stdout)
    pickle.dump(labels,sys.stdout)
    pickle.dump(counts,sys.stdout)
    
        
    