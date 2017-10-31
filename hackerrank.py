#!/bin/python3

import sys

n = int(input('Enter N:').strip())
a = []

for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input('Enter a:')]
    a.append(a_t)
print (a)