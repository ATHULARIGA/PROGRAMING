# class Book:
#   """A class to represent a book."""

#   def __init__(self, title, author, genre, year):
#     self.title = title
#     self.author = author
#     self.genre = genre
#     self.year = year

    

  
  


# class Library:
#     def __init__(self):
#         self.book=[]

#     def add_book(self, book):
#         self.book.append(book)
    
#     def search_By_Title(self, title):
#         matching_books = []
#         for book in self.book:
#             if title.lower() in book.title.lower():
#                 matching_books.append(book)
#         return matching_books
#     def list_all_books(self):
#             print(book)
# library =Library()

# library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 1954))
# library.list_all_books()
def add_book():
    book=[]
    title=input("enter title name:")
    author=input("enter name of author :")
    info=[title, author]
    if title not in book:
        book.append(info)
    print(book)


def menu():
    print("1: For adding new book\n2: Search for book\n3: List of Book\n4: Exit ")
    choice=int(input("enter the  choice:"))
    if choice==1:
        add_book()
        menu()
    elif choice==2

menu()


