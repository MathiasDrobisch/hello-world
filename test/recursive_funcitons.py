# recursive code python
# Hackerrank ex 9

import sys

def factorial(n):
  if n == 1:
      return 1
  else:
      return n * factorial(n-1)

if __name__ == "__main__": # this is trigger if the script is exerised on its own,
#not imported into another script to run there, than this block wont return
    n = int(input().strip())
    result = factorial(n)
    print(result)


# Hakerrank ex 4 - classes in python
class Person:
    def __init__ (self, initialAge):
        # code runs a check against input initialAge
        self.age = initialAge
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0

    def amIOld(self):
        # logic to return printed statement
        if self.age < 13:
            print('You are young.')
        elif 13 <= self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old')
    def yearPasses(self):
        # Increment age by one year
        self.age += 1
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
