def whats_on_tv(penguine=None):
    if penguine is None:
        penguine = []
    penguine.append('property of the zoo')
    print(penguine)

whats_on_tv() # to call a function simply write it down


# Loop with Continue statement, which follows through even if the if-statements
# is not fullfilled

for num in range(2,10):
    if num % 2 == 0:
        print('found an even number')
        continue
    print('found an uneven number')

# pass statement, does nothing but is used where sythatically a statement is necessary
def new_function():
    pass # remember to implement this



def fib(n):
    """Prite a Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function
fib(2000)

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, b+a
    return result

print(fib2(100))
