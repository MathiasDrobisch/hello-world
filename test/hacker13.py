# Map function
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)
# lambda creates a function without a name on the fly
# map (function to be applied, items function applies)

# Hackerrank task 13 - Abstract Class methods
from abc import ABCMeta, abstractmethod #ABC = Abstract Base Class
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass


#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self,title,author)
        self.price = price

    def display(self):
        print('Title:', title)
        print('Author:', author)
        print('Price:', price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
