# TASK: We have T test cases, for each test case we input a String and print the even and odd indexed letters
# Exercise 6 Hackerrank
# Combine loops and strings
import sys

for i in range(int(input())):
    s = input()
    print(s[::2],s[1::2]) # prints even and odd letters
