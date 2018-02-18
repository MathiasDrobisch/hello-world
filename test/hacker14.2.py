#hacker exercise 14

class Difference:
    # A class constructor that takes an array of int as parameter
    # and saves them to elements instance variable
    def __init__(self, a):
        self.__elements = a
    # method to find max absolute difference between any N numbers
    # and stores it in maximumDifference instance variable
    def computeDifference(self):
    	self.maximumDifference=max(a)-min(a)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
