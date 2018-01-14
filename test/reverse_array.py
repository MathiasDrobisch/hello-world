#!/bin/python3

import sys


#n = int(input().strip())
#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#print(" ".join(map(str, arr[::-1])))
x = []
for test in input().strip().split(' '):
    x.append(int(test))
print(" ".join(map(str, x[::-1])))


def f(a,L=[]): # the following function accumulates the arguments passed to it on subsequent calls:
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))


def ask_ok(prompt, retries = 4, reminder = 'Please try again.'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really like me?',1)
