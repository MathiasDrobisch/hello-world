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
    except EOFError: # EOFError means end of file error
    #when the input file ends, this error will be shown and the
    # infinte loop is exited
        break
