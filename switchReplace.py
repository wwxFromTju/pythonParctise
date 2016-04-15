#!/usr/bin/env python
def getTheLevel(score) :
    level = {
        10 : 'A',
        9 : 'A',
        8 : 'B',
        7 : 'C',
        6 : 'D'
    }
    return level.get(score/10,'F')
print getTheLevel(90)
print getTheLevel(100)
print getTheLevel(91)
print getTheLevel(89)
print getTheLevel(80)
print getTheLevel(70)
print getTheLevel(60)
print getTheLevel(59)