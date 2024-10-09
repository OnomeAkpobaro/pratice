class Bird:
    def fly(Bird):
        return "The bird is flying"
class Mammal:
    def run(Mammal):
        return "The mammal is running"
class Bat(Bird, Mammal):
    pass
    def fly(self):
        print("The bat is flying swiftly")
    def run(self):
        print("The bat is crawling slowly")
bat = Bat()
bat.fly()
bat.run()
