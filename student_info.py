class student:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

        
    def display_info(self):
            print(f"{self.name} is {self.age} years old. ")
            

student1 = student("John Doe", "20")
student2 = student("Bekky Matt","19")
student1.display_info()
student2.display_info()