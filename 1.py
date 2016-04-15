#!/usr/bin/env python
a = int(raw_input('enter a'))
b = int(raw_input('enter b'))
c = int(raw_input('enter c'))

a,b = (a,b) if a > b  else (b,a)
b,c = (b,c) if b > c else (c,b)

print c,b,a