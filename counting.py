class Book:
    count = 0           #class variable for count instance
    def __init__(self, total_books):
        self.total_books = total_books
        Book.count += 1         #increament count on instance count


    @classmethod
    def display_total_books(cls):
        print(f"Total Books: {cls.count}")

book1 = Book('Andy and the lady')
book2 = Book('Tega is beautiful')
book3 = Book('I have a lot of money')
Book.display_total_books()