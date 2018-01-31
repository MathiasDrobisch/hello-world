class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        if sum(self.scores)/len(self.scores) < 40:
            return('T')
        elif sum(self.scores)/len(self.scores) < 55:
            return('D')
        elif sum(self.scores)/len(self.scores) < 70:
            return('P')
        elif sum(self.scores)/len(self.scores) < 80:
            return('A')
        elif sum(self.scores)/len(self.scores) < 90:
            return('E')
        else:
            return('O')

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

scores = list( map(int, input().split()) )
print(scores)
