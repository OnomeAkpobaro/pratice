# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"Person {self.name}, {self.age} years old.")
#     def __del__(self):

#         print("Deleted...")
# person1 = Person("Jhon", 55)
# print(person1)



# class Book:
#     def __init__(self, title, author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

# book1 = Book("Jack and Jill", "Matt", 20)
# print(book1)


class Animal:
    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")
    
    def make_sound(self):
        print("Woof!")
        
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
animals = [Dog(), Animal()]
ringo = Dog("Ringo")


for animal in animals:
    animal.make_sound()


