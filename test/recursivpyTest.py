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
