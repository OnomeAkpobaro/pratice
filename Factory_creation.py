class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    @classmethod
    def create_child(cls, name):
        return cls(name, 0)
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

adult = Person("John", 39)
child = Person.create_child("Baby John")

adult.display_info()
child.display_info()
        