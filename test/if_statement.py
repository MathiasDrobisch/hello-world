x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative values changed to 0')
elif x == 0:
    print('You chose Zero')
elif x == 1:
    print('Really just 1')
else:
    print('large numbers, I like it')

words = ['cat', 'window', 'defenestrate']

print('Now comes a for loop of 3 words and their responding length:')
for w in words:
    print(w, "- the word as a lenght of", len(w))

# If you do need to iterate over a sequence of numbers, the built-in function range()
print('Now comes a for loop of range 5:')
for i in range(5):
    print(i)
print('You see 5 is not included in the range')
print('Now comes a for a check of prime numbers, range to be checked defined by the user:')
user_input = int(input("please input a number between 1-100: "))
# break clause and loops
for n in range(2,user_input): # range is not inclusive of the endings, i.e. 2 and user_input in this case!
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        #loop fell through without finding a factor
        print(n, 'is a prime number')
# When used with a loop, the else clause has more in common with the else clause of
# a try statement than it does that of if statements: a try statement’s else clause runs when no exception occurs,
# and a loop’s else clause runs when no break occurs.
tel = {'jack': 4098, 'sape': 4139}
print(tel)
