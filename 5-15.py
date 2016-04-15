#!/usr/bin/env python

def maxDivisor(num1, num2) : 
    if num1 % num2 :
        return maxDivisor(num2, num1 % num2)
    else : 
        return num2

def minMultiple(num1, num2):
    return num1 * num2 / maxDivisor(num1, num2)

if __name__ == "__main__" : 
    print maxDivisor(15, 25)
    print maxDivisor(25, 15)
    print minMultiple(3,4)
    print minMultiple(10,15)

