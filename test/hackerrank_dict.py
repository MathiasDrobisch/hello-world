# Second try
n = int(input())
name_numbers = [input().split() for x in range(n)]
print(name_numbers)
phoneBook = {k:v for k,v in name_numbers}
# combine line 2 and 4: phoneBook = dic(input().split() for _ in range(n))
print(phoneBook)
while(1):
    try:
        name = input()
        if name in phoneBook:
            print("{}={}".format(name,phoneBook[name]))
        else:
            print('Not found')
    except:
        break

# Third version
#number of entries in phonebook
n = int(input().strip())
phoneBook3 = {}

#assign in phoneBook
for _ in range(n): # _ is a throwaway variable
    nam, num = input().strip().split(' ')
    phoneBook3[nam] = num

#query phoneBook while there is input, exit when EOF
while(1):
    try:
        qName = input().strip()
        if qName in phoneBook3:
            print("{}={}".format(qName,phoneBook3[qName]))
        else:
            print('Not found')
    except EOFError:
        break

# MY TRY: does not allow changing numbers of values
phoneBook = {'sam':99912222,'tom':11122222,'harry':12299933}
testNames = ['sam', 'edward', 'harry']

for test in testNames:
        if test not in phoneBook:
            print('Not found')
        else:
            print("{}={}".format(test,phoneBook[test]))
