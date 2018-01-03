import sys

script, first, second, third = sys.argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name') # the r in front of the string reminds the system that this is a raw print

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

indexing = 'Python'
print(indexing[0])
print(indexing[2])
print(indexing[-1])
