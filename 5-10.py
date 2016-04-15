#!/usr/bin/env python

from __future__ import division

def transformF2C(F) : 
    return (F - 32) * (5 / 9)

if __name__ == "__main__" : 
    print transformF2C(100)