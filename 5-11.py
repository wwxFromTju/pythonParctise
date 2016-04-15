#!/usr/bin/env python

def calEven( numrange ) :
    return [even for even in numrange if even % 2 == 0]

def calOdd( numrange ):
    return [odd for odd in numrange if odd % 2 == 1]

def isDivision(num1, num2):
    return True if num1 % num2 == 0 else False

if __name__ == "__main__" : 
    print calEven(range(21))
    print calOdd(range(22))
    print isDivision(4, 2)
    print isDivision(4, 3)