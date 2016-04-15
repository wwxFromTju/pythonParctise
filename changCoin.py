#!/usr/bin/env python
def changeCoin(num) : 
    num_25 =  num // 0.25
    num -= num_25 * 0.25
    num_10 = num // 0.1
    num -= num_10 * 0.1
    num_1 = int(num * 100)
    return num_25,num_10,num_1

print changeCoin(0.9)
print changeCoin(0.01)