class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"{self.name} ({self.birthday}), {self.country}"

    def __repr__(self):
        return f"Author('{self.name}', '{self.country}', '{self.birthday}')"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1
        author.books.append(self)

    def __str__(self):
        return f"{self.name} ({self.year}), by {self.author.name}"

    def __repr__(self):
        return f"Book('{self.name}', {self.year}, {self.author})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books"

    def __repr__(self):
        return f"Library('{self.name}')"



author1 = Author("Author 1", "Country 1", "01-01-1990")
author2 = Author("Author 2", "Country 2", "02-02-1995")

library = Library("My Library")

book1 = library.new_book("Book 1", 2000, author1)
book2 = library.new_book("Book 2", 2005, author2)
book3 = library.new_book("Book 3", 2000, author1)

print(library)
print(author1)
print(author2)
print(book1)
print(book2)
print(book3)


print(library.group_by_author(author1))
print(library.group_by_year(2000))
