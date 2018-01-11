import sys

# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'a', 'test', 'more_test']

for i in range(len(a)):
    print(i,a[i])

# striping all blanc spaces before and after the string, or in this case the 0
str = "0000000this is string example....wow!!!0000000";
print (str.strip('0'))

# FOR loop
n = int(input().strip())
for i in range(1,11):
    print(n, '*', i, '=', n*i)

# WHILE loop is like a repeated if statement, as long as the condition is TRUE
# it will run the code block repeatedly
x=0
i=int(input().strip())
while (x<i):
    print('the value of x is ', x)
    x= x+1
else:
    print('x is larger than ',i)

# List is being mutable sequence that is going to be changed through the loop
a = [0, 1, 2, -4, -7, 9, -1, 3]

for x in a[:]:
    if x < 0:
        a.remove(x) # removes the value x of the list, this means if a value meets the condition its being removed
                    # from the List
print(a, 'list does not contain any negatives anymore, removed by for loop)
