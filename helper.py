#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 19:10:21 2017

@author: Nuoyu Li (nuoyul@andrew.cmu.edu)
"""

import re

def tokenizeDoc(cur_doc):
    return re.findall('\\w+',cur_doc)

def get_labels(labelstr):
    # get labels that end with "CAT" from the string of labels
    return [word for word in labelstr.split(',') 
            if word.endswith("CAT")]
    