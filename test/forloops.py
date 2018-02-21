#print(list(range(5)))

#for number in [0,1,2,4]:
#    print(number)

count = 0
for number in range(1,4):
    count = count + number

print(count)

def sum_list(my_list):
    count = 0
    for number in my_list:
        count = count + number
    return count

assert sum_list([1,2,3]) == 6 # brings up an error if the test is wrong
assert sum_list([1,3]) == 4

# running the script does not cause an error

# While loops
# Used if you don't know how long something runs

count = 0
while count < 100:
    count = count + 1
    print(count)

# Exception Handling
import sys

S = input().strip()
try:
    print(int(S))
except ValueError:
    print("Bad String")
