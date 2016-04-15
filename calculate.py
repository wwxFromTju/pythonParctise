#!/usr/bin/env python

def calculate(str) : 
    def add(a, b) : 
        return a + b
    def  sub(a, b):
        return a - b
    def mul(a, b):
        return a * b
    def div(a, b):
        return a / b
    def power(a, b):
        return a ** b
    mapToFun = { 
        "+": add,
        "-" : sub,
        "**" : power,
        "/" : div,
        "*" : mul
        }
    for temp in mapToFun :
        if temp in str : 
            if "**" in str:
                temp = "**"
            listNum = str.split(temp)
            return mapToFun[temp](int(listNum[0]), int(listNum[1]))

print calculate('1+2')
print calculate('1-2')
print calculate('1*2')
print calculate('1/2')
print calculate('1**2')