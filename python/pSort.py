#!/usr/bin/python 
# -*- coding:Utf-8 -*- 

import sys
def keynat(string):
    r'''A natural sort helper function for sort() and sorted()
    without using regular expressions or exceptions.

    >>> items = ('Z', 'a', '10th', '1st', '9')
    >>> sorted(items)
    ['10th', '1st', '9', 'Z', 'a']
    >>> sorted(items, key=keynat)
    ['1st', '9', '10th', 'a', 'Z']    
    '''
    it = type(1)
    r = []
    for c in string:
        if c.isdigit():
            d = int(c)
            if r and type( r[-1] ) == it: 
                r[-1] = r[-1] * 10 + d
            else: 
                r.append(d)
        else:
            r.append(c.lower())
    return r


try:
	fichier=sys.argv[1]
except:
	sys.exit()
listTab = open(fichier,'r').readlines()
listTab.sort(key=keynat)
open(fichier,'w').writelines(listTab)
