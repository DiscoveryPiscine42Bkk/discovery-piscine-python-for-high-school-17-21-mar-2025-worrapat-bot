#!/usr/bin/env python3
a = [2, 8, 9, 48, 8, 22, -12, 2]
b = [i+2 for i in a]
c = [i for i in b if i > 5]
print(a)
print(c)

