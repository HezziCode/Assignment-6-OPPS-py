class Book:
    total_book = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_book += 1

    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

b1 = Book("Dreams", "Altaf Hussian")
b2 = Book("The Alchemist", "Paulo Coelho")

print(f"\n{Book.total_book} books were created.")