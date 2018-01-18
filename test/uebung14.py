from sys import argv

script, filename = argv

txt = open(filename)
print(filename)
print("Here is your file {}".format(filename))

print(txt.read())

print('type filename again:')

file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
