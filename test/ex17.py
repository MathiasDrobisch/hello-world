from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(from_file, to_file)
print('Copying from %s to %s' % (from_file, to_file))

#we could do these on one line
in_data = open(from_file).read()

print('The input file is %d bytes long' % len(in_data))

print('Does the output file exist? %r' % exists(to_file))

print('Ready, hit Return, to contiue, CTRL-C to abort')

input()

out_file = open(to_file, 'w')

out_file.write(in_data)

print('Alright done')
out_file.close()
