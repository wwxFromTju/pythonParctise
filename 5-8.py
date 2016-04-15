#!/usr/bin/env python
import math
def calSequalArea(edge) : 
    return edge ** 2;

def calSequalBulk(edge):
    return edge ** 3;

def circleArea(radius):
    return math.pi * ( radius ** 2 )

def circleBulk(radius):
     return math.pi * ( radius ** 3 ) * 3.0/ 4.0


if __name__ == "__main__" : 
    print circleArea(1)
    print circleBulk(1)
    print calSequalArea(1)
    print calSequalBulk(1) 