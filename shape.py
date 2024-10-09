class Shape:                   
    def calculate_area(self):
         return "Area not defined."
    
class Rectangle(Shape):
        def __init__(self, length, breadth):
            self.length = length 
            self.breadth = breadth
        def calculate_area(self):
            return self.breadth * self.length
        




rectangle = Rectangle(5,10)
area = rectangle.calculate_area()
print(f"Area of the rectangle: {area}")
        
