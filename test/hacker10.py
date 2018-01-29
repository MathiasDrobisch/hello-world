import sys
import re #regex module

# Exercise 10
n = len(max(re.split('0+',bin(int(input().strip()))[2:])))

print(n)

print(bin(int(input())))
