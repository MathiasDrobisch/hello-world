import sys

# Python notes on Matrix
matrix = [
[1,2,3,0],
[0,6,0,0],
[3,4,5,0],
[0,0,0,0]
]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
print('------zip statement:')
print(list(zip(*matrix))) # this creates a list of tuples, not a list of lists

# Hackerank task 11: Calculation of hourglass
# TASK: Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
arr = []
for arr_i in range(4):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')] # we loop through the lists that are inputed
   arr.append(arr_t)
print('------input Matrix statement:')
print(arr)

resultmatrix = []
for row in range(0,2):
    for column in range(0,2):
        total = sum(arr[row][column:column+3]) + arr[row+1][column+1] + sum(arr[row+2][column:column+3])
        resultmatrix.append(total)
print(max(resultmatrix))
