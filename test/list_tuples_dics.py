test = 'hello world'
print(test[:]) # prints out the whole list
print(test[2:5])
print(test[6:15])

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][1]) #meaning take first element 0 and of that element the element 1

# Output: 5
print(n_list[1][3])

list = ['abcd', 123, 'john', 23, 43, 'test']
tinylist = ['test2', 567]

print(list)
print(list[0])
print(list + tinylist)

"""The main differences between lists and tuples are:
Lists are enclosed in brackets ( [ ] )
and their elements and size can be changed,
while tuples are enclosed in parentheses ( ( ) )
and cannot be updated. Tuples can be thought of as read-only lists."""

tuples = (123,'test', 'asdf', 134, 'asdfkl')
tinytuples = (456,'test4365')

print(tinytuples+tuples)
print(tuples[2])
print(tinytuples[0])

#tinytuples[0] = 1000
tinylist[0] = 1000
print(tinylist)
print(tinytuples)

dict = {}
dict['one'] = 'this is one'
dict[2] = 'well this is two'

tinydict = {'name':'john', 'code':1123, 'dept':'Marketing'}

print(dict)
print(tinydict)
print(tinydict.keys)
print(tinydict.values)
print(dict['one'])
print(tinydict['name'])

#Decision making in Python
var = 100
if (var == 100):
    print('value of variable is 100')
