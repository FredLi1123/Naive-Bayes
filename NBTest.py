#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:15:51 2017

@author: Nuoyu Li (nuoyul@andrew.cmu.edu)
"""

from __future__ import division, print_function 
import sys
import math
import helper

def readcounts():
    labels = []
    counts = {}
    # use a set to eliminate duplicated words
    words = set()
    
    line = sys.stdin.readline()
    while line:
        # split each line by tab to get keys and counts 
        entry = line.split('\t',1)
        key = entry[0]
        count = entry[1]
        
        # convert count to actual integer
        counts[key] = int(count)
        
        """
        if - collect all labels
        elif - collect all words
        """
        if ',' not in key and key != '*': 
            labels.append(key)
        elif ',' in key:
            word = key.split(',')[1]
            if word != '*':
                words.add(word)
        
        line = sys.stdin.readline()      
    
    return len(words),labels,counts
            
def readcommandline():
    """
    read the testfile from the second command line argument;
    the first argument is python script
    """
    try: 
        inputtestfile = open(sys.argv[1],'r') 
        return inputtestfile 
    except Exception: 
        print('invalid testfile directory, try again') 
        print('usage: python NBTest.py <testfile>') 
        sys.exit(2)

def extractinfo(document):
    # similar to the function in training file
    parts = document.split('\t',1)
    labels = parts[0].split(',')
    words = helper.tokenizeDoc(parts[1])
    
    return labels, words

def test(testfile,V,labels,counts):
    currentdoc = testfile.readline()
    L = len(labels) # total number of labels
    
    correctdocs = 0
    totaldocs = 0
    
    while currentdoc:
        #currentdoc = bytes(currentdoc, 'utf-8').decode('utf-8', 'ignore')
        current_labels, words = extractinfo(currentdoc)
        
        # if no label ending with "CAT", skip the document
        if len([l for l in current_labels 
                if l.endswith("CAT")]) == 0:
            currentdoc = testfile.readline()
            continue
        
        # python 3: maxprob = math.nan
        maxprob = float('nan')
        testlabel = ''
        
        # otherwise, calculate the smoothed log probability for each label
        for l in labels:
            prior = math.log(counts[l]+1)-math.log(counts['*']+L)
            posterior = 0
            
            for w in words:
                if l+','+w in counts:
                    posterior = posterior+math.log(
                            counts[l+','+w]+1)-math.log(counts[l+',*']+V)
                else:
                     posterior = posterior-math.log(counts[l+',*']+V) 
            
            # update maximum log-probability and label assignment
            maxprob = max(prior+posterior,maxprob)
            if maxprob == prior+posterior: testlabel = l
        
        # format the output - tab separated, 4-digit log probability
        print(str(current_labels)+'\t'
              +str(testlabel)+'\t'
                  +"{0:.4f}".format(maxprob))
       
        if testlabel in current_labels: correctdocs += 1
        totaldocs += 1
        
        currentdoc = testfile.readline()
    
    testfile.close()
    # calculate accuracy
    print('Percent correct:\t'+
          str(correctdocs)+'/'+str(totaldocs)+'='+
             "{0:.4f}".format(correctdocs/totaldocs))

if __name__ == '__main__':
    V,labels,counts = readcounts()
    testfile = readcommandline()
    test(testfile,V,labels,counts)