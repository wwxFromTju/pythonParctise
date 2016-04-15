#!/usr/bin/env python

total = input("Enter opening balance : ")
everyMonth = input("Enter monthly payment : ")

print " " * 8 , "Amount", " " * 2, "Remaining"
print "Pymt#", " " * 3, "Paid"," " * 4,"Balance"
print "-" * 24

i = 0
temp = total
while temp > 0 :   
    leftMoney = total - i *  everyMonth
    temp = leftMoney if leftMoney > 0 else 0
    paid = everyMonth  if temp > 0 else leftMoney + everyMonth
    paid = 0 if i == 0 else paid
    print "%d       $ %.2f        %.2f" % (i, paid, temp)
    i += 1 