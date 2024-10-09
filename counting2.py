class Book:
    count = 0
    book_titles = []

    def __init__(self, title_books):
       
        self.title_books = title_books
        Book.count += 1
        Book.book_titles.append(self.title_books)


    
    @classmethod
    def display_count(cls):
        print(f"Total Books: {cls.count}")
        print("Book Titles:")
        for title in cls.book_titles:
            print(f"- {title}")

book1 = Book("Andy and the chips")
book2 = Book("Tega Tega")
book3 = Book("Take it there")

Book.display_count()
