#python classes 1 
class StringManipulator:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

obj = StringManipulator()
obj.getString()
obj.printString()

#python  classes 2 
class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)

length = int(input())
sq = Square(length)
sq.area()

#python classes 3
class Shape:
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
length = int(input())
width = int(input())
rect = Rectangle(length, width)
rect.area()

#python classes 4 
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)** 2 + (self.y - other_point.y)**  2)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
p1 = Point(x1, y1)
p2 = Point(x2, y2)
p1.show()
p2.show()
print(f"Distance between points: {p1.dist(p2)}")

#python classes 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")

owner = input("Enter account owner: ")
balance = float(input("Enter initial balance: "))
acc = Account(owner, balance)

while True:
    action = input("Enter 'deposit' to deposit, 'withdraw' to withdraw, or 'exit' to exit: ").lower()
    if action == 'deposit':
        amount = float(input("Enter deposit amount: "))
        acc.deposit(amount)
    elif action == 'withdraw':
        amount = float(input("Enter withdrawal amount: "))
        acc.withdraw(amount)
    elif action == 'exit':
        break
    else:
        print("Invalid action")

#python classes 6
numbers = list(map(int, input().split()))
prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) if x > 1 else False, numbers))
print("Prime numbers:", prime_numbers)

#functions1 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input("Enter the amount in grams: "))
ounces = grams_to_ounces(grams)
print({ounces})

#functions1 2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}° Fahrenheit is equal to {celsius}° Celsius.")

#functions1 3
def solve(numheads, numlegs):
    chickens = (numlegs - 4 * numheads) // -2
    rabbits = numheads - chickens
    return chickens, rabbits
numheads = int(input("Enter the number of heads: "))
numlegs = int(input("Enter the number of legs: "))

chickens, rabbits = solve(numheads, numlegs)
print(f"There are {chickens} chickens and {rabbits} rabbits.")

#functions1 4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

numbers = list(map(int, input().split()))
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

#functions1 5
import itertools
def print_permutations(string):
    permutations = itertools.permutations(string)
    for perm in permutations:
        print(''.join(perm))

string = input("Enter a string: ")
print_permutations(string)

#functions1 6
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))
sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)

#functions1 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
result = has_33(nums)
print(result)

#functions1 8
def spy_game(nums):
    sequence = [0, 0, 7]
    for i in range(len(nums) - 2):
        if nums[i:i+3] == sequence:
            return True
    return False

nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
result = spy_game(nums)
print(result)

#functions1 9

import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print({volume})

#functions1 10

def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
unique_lst = unique_elements(lst)
print("List with unique elements:", unique_lst)

#functions1 11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
word_or_phrase = input("Enter a word or phrase: ")
if is_palindrome(word_or_phrase):
    print(f"'{word_or_phrase}' is a palindrome.")
else:
    print(f"'{word_or_phrase}' is not a palindrome.")

#functions1 12 

def histogram(lst):
    for num in lst:
        print('*' * num)

lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
histogram(lst)

#functions1 13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number_to_guess = random.randint(1, 20)
    guess_count = 0
    guessed = False
    while not guessed:
        print("Take a guess.")
        guess = int(input())
        guess_count += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            guessed = True
            print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")

guess_the_number()

#functions2 1
def is_imdb_above_5_5(movie):
    return movie["imdb"] > 5.5


#functions2 2
def filter_movies_by_imdb(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

#functions2 3
def filter_movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

#functions2 4
def average_imdb_score(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies) if movies else 0


#functions2 5
def average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"] == category]
    if category_movies:
        total_score = sum(movie["imdb"] for movie in category_movies)
        return total_score / len(category_movies)
    else:
        return 0
