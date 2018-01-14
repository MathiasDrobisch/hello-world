# Example break clause in if statement
for letter in 'Python':
    if letter == 'h':
        break
    print('current letter :', letter)

# Second Example
var = 10
while var > 0:
    print ('Current variable value :', var)
    var = var - 1
    if var == 5:
        break

print('Good bye!')


# Contiune statements
for letter in 'python':
    if letter == 'h':
        continue
    print("Current Letter :", letter)

#second Example
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue # continue here moves the iteration back to the top of the loop here
        # that means the 5 is not printed and the loop starts again at while
    print('Current variable value :', var)

print('Good bye')

#nested loops - clever way to find prime numbers
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if (i%j) == 0 : break # if not clause possible too. if not (i%j): break
        # if not enters into iteration when the condtion is false (0)
        j = j + 1
    if (j > i/j): print(i, 'is a prime')
    i = i + 1
