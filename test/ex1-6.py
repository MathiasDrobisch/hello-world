print("Hello World")
print("Hello Again")
print("I like this.")
print("This is fun.")
print('yah, much better.')
print("I would much rather you 'not'")

print('I could like this.')  # test test nothing happens with that

print('I will now count mz chickens:')
print('Hens', 25 + 30 / 6)
print('roosters', 100 - 25 * 3 % 4)
print('Now i will count my eggs:')
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print('Is it greater?', 5 > -2)
print('is it greater or equal?', 5 >= -2)
print('Is it less or equal?', 5 <= -2)

print(3 % 4)
print(25 * 3)
print(25 * 3 % 4)

cars = 100
space_in_the_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_the_car
average_passengers_per_car = passengers / cars_driven

print('there are', drivers, 'drivers availabe')
print('There are only', cars, 'cars available.')
print('We can transport', carpool_capacity, 'people today')
print('We have', passengers, 'to carpool today')
print('We need to put about', average_passengers_per_car, 'in each car')

my_name = 'Mathias'
my_age = 28  # not a lie
my_height = 175  # centimeter
my_weight = 70
my_eyes = 'blue'
my_teeth = 'white'

my_hair = 'brown'

print(f"let's talk about {my_name}")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight}")

total = my_age + my_height + my_weight
print(f'if I add {my_age}, {my_height} and {my_weight} i get {total}')

types_of_people = 10
x = f'there are {types_of_people} types of people.'
binary = 'binary'
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: '{x}'")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke funny? {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "A string with a right side"

print(w + e)
