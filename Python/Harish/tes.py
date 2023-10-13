class Book:
  """A class to represent a book."""

  def __init__(self, title, author, genre, year):
    self.title = title
    self.author = author
    self.genre = genre
    self.year = year

  def __str__(self):
    return f"{self.title} by {self.author}"


class Library:
  """A class to represent a library."""

  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def remove_book(self, book):
    self.books.remove(book)

  def search_books_by_title(self, title):
    matching_books = []
    for book in self.books:
      if title.lower() in book.title.lower():
        matching_books.append(book)
    return matching_books

  def search_books_by_author(self, author):
    matching_books = []
    for book in self.books:
      if author.lower() in book.author.lower():
        matching_books.append(book)
    return matching_books

  def list_all_books(self):
    for book in self.books:
      print(book)


# Example usage:
library = Library()

# Add some books to the library
library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 1954))
library.add_book(Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction", 1979))
library.add_book(Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", 1997))

# Search for books by title
matching_books = library.search_books_by_title("Harry Potter")

# Print the matching books
for book in matching_books:
  print(book)

# List all books in the library
library.list_all_books()
