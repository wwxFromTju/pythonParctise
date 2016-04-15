#!/usr/bin/env python

'makeTextFile.py -- create text file '

import os 
ls = os.linesep

help = '''
    enter you want : 
    Read file : r
    Write file : w
'''
operator = ['r', 'w']
enter = ''

while enter not in operator : 
    enter = raw_input(help)
if enter == 'w':
    #get filename
    while True:
        fname = raw_input("enter your file name : ")
        # if os.path.exists(fname) :
        try :
            open(fname,"r")
            print "ERROR '%s' already exists" % fname
        except IOError, e : 
            break
    all = []
    print "\nEnter lines ('.' by itself to quit) . \n"

    #loop until user terminates input
    while True:
        enter = raw_input('> ')
        if enter == '.' : 
            break
        else : 
            all.append(enter)

    fobj = open(fname,'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all ])
    fobj.close()

    print "DONE"
else :
    'readTextFile.py -- read and display text file'

    # get filename
    fname = raw_input('Enter filename: ')
    print

    #attempt to open file for reading 
    if os.path.exists(fname):
        fobj = open(fname, 'r') 
        #display contents to the screen
        for eachLine in fobj :
            eachLine = eachLine[:-1]
            print "%s" % eachLine
        fobj.close() 
    else:
        print "*** file open error: "
