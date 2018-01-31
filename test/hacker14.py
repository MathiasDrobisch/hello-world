# Looping through the numbers 2-10 to find prime numbers
for n in range(2, 10): # 10 is not taking into account for the range, the 2 however yes)
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# Use of lambda and map(), reduce(), filter()
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

mapping = list(map(lambda x: x * 2, foo))
print ('This is the mapping fuction:', mapping)

filtering = list(filter(lambda x: x % 3 == 0, foo))
print('This is the filtering function:', filtering)

sentence = 'It is raining cats and dogs'
words = sentence.split()

wordLength = list(map(lambda x: len(x), words))
print('Longest word in the sentecne is',max(wordLength), 'letters long')
print('longest word in list is {} letters long'.format(max(wordLength)))
print('longest word in list is %s letters long' % max(wordLength))
