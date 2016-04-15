#!/usr/bin/env python

def isLeapYear(year) : 
        if year % 400 == 0 :
            answer = 'leap'
        elif year % 4 == 0 and year % 100 != 0:
            answer = 'leap'
        else : 
            answer = 'no leap'
        return answer
print isLeapYear(1992)
print isLeapYear(1996)
print isLeapYear(2000)
print isLeapYear(1967)
print isLeapYear(1900)
print isLeapYear(2400)

