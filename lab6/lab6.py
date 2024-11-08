import math

#1
class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Using Heron's formula for area of a triangle
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())

#2
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient funds or invalid amount."

class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of {interest} added. New balance is {self.balance}."


class CheckingAccount(Account):
    def __init__(self, balance=0, overdraft_limit=0):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        else:
            return "Insufficient funds or overdraft limit exceeded."


savings = SavingsAccount(1000, interest_rate=0.05)
print(savings.deposit(200))
print(savings.withdraw(500))
print(savings.calculate_interest())

checking = CheckingAccount(500, overdraft_limit=100)
print(checking.deposit(100))
print(checking.withdraw(700))
print(checking.withdraw(50))

#3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, mpg):
        super().__init__(make, model, year)
        self.mpg = mpg

    def calculate_mileage(self, miles):
        return f"Fuel used: {miles / self.mpg:.2f} gallons."


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mpg):
        super().__init__(make, model, year)
        self.mpg = mpg

    def calculate_mileage(self, miles):
        return f"Fuel used: {miles / self.mpg:.2f} gallons."


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def towing_info(self):
        return f"Towing capacity: {self.towing_capacity} lbs"

car = Car("Toyota", "Camry", 2022, 30)
motorcycle = Motorcycle("Honda", "CBR500R", 2021, 60)
truck = Truck("Ford", "F-150", 2023, 13000)

print(car.display_info())
print(car.calculate_mileage(300))

print(motorcycle.display_info())
print(motorcycle.calculate_mileage(300))

print(truck.display_info())
print(truck.towing_info())

#4
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        return f"Employee ID: {self.id}, Name: {self.name}"


class Manager(Employee):
    def __init__(self, name, id, salary, department):
        super().__init__(name, id)
        self.salary = salary
        self.department = department

    def display_role(self):
        return f"Manager of {self.department}, Salary: ${self.salary}"


class Engineer(Employee):
    def __init__(self, name, id, salary, field):
        super().__init__(name, id)
        self.salary = salary
        self.field = field

    def display_role(self):
        return f"Engineer in {self.field}, Salary: ${self.salary}"


class Salesperson(Employee):
    def __init__(self, name, id, salary, region):
        super().__init__(name, id)
        self.salary = salary
        self.region = region

    def display_role(self):
        return f"Salesperson for {self.region}, Salary: ${self.salary}"

manager = Manager("Alice", 101, 90000, "HR")
engineer = Engineer("Bob", 102, 80000, "Software")
salesperson = Salesperson("Char", 103, 50000, "West Coast")

print(manager.display_info())
print(manager.display_role())

print(engineer.display_info())
print(engineer.display_role())

print(salesperson.display_info())
print(salesperson.display_role())

#5
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "This animal makes a sound."


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def sound(self):
        return "This mammal makes a specific sound."

class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span

    def sound(self):
        return "Chirp chirp!"

class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type

    def sound(self):
        return "Fish don't make audible sounds!"

mammal = Mammal("Lion", "Golden")
bird = Bird("Eagle", "2 meters")
fish = Fish("Shark", "Saltwater")

print(f"{mammal.name} has {mammal.fur_color} fur.")
print(mammal.sound())

print(f"{bird.name} has a wingspan of {bird.wing_span}.")
print(bird.sound())

print(f"{fish.name} lives in {fish.water_type} water.")
print(fish.sound())

#6
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} checked out."
        return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} returned."
        return f"{self.title} was not checked out."

    def display_info(self):
        return f"Title: {self.title}, ID: {self.item_id}, Checked out: {self.checked_out}"

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        return super().display_info() + f", Author: {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director):
        super().__init__(title, item_id)
        self.director = director

    def display_info(self):
        return super().display_info() + f", Director: {self.director}"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue

    def display_info(self):
        return super().display_info() + f", Issue: {self.issue}"

book = Book("The Great Gatsby", 1001, "F. Scott Fitzgerald")
dvd = DVD("Inception", 2001, "Christopher Nolan")
magazine = Magazine("National Geographic", 3001, "March 2024")

print(book.display_info())
print(book.check_out())
print(book.return_item())

print(dvd.display_info())
print(dvd.check_out())

print(magazine.display_info())
print(magazine.check_out())
