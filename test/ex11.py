print('How old are you?'),
age = input()
print('How tall are you?'),
height = input()
print('How much you weight?'),
weight = input()

print('So you are %r old, %s tall and %s heavy' % (age, height, weight))

# A different way of inputs into a function with the .format
print('So you are {} old, {} tall and {} heavy'.format(age, height, weight))

# It is possible to write the string immidiately into the input function
age2 = input("How old are you? ")
print(age2)
