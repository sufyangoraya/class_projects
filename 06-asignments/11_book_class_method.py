class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        print(f"Total Books: {cls.total_books}")

# Example
b1 = Book()
b2 = Book()
Book.increment_book_count()
