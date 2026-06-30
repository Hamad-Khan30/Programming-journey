class Book:
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        if self.year:
            return f"'{self.title}' by {self.author} ({self.year})"
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return self.__str__()

class Library:
    def __init__(self, name="My Library"):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)
        print(f"Added: {book}")
    
    def list_books(self):
        """List all books in the library"""
        if not self.books:
            print(f"{self.name} is empty!")
            return
        
        print(f"\n📚 {self.name} - All Books:")
        print("-" * 40)
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print("-" * 40)
        print(f"Total: {len(self.books)} books\n")
    
    def find_by_author(self, author_name):
        """Find all books by a specific author"""
        found_books = [book for book in self.books if book.author.lower() == author_name.lower()]
        
        if found_books:
            print(f"\n📖 Books by '{author_name}':")
            for book in found_books:
                print(f"  • {book}")
            print()
        else:
            print(f"No books found by '{author_name}'\n")
        
        return found_books
    
    def __str__(self):
        return f"{self.name} ({len(self.books)} books)"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("1984", "George Orwell", 1949)
book4 = Book("Animal Farm", "George Orwell", 1945)
book5 = Book("Pride and Prejudice", "Jane Austen", 1813)
book6 = Book("The Hobbit", "J.R.R. Tolkien", 1937)

my_library = Library("City Central Library")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)
my_library.add_book(book6)

my_library.list_books()

my_library.find_by_author("George Orwell")
my_library.find_by_author("J.K. Rowling")  

print(my_library)




