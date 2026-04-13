#Write a program to create a menu-driven 
# Library Management System that can do these four tasks 
# - display a book, 
# lend or return a book 
# and add a book.
#  Make use of OOPs concepts,
#  loops and conditional statements
#  wherever required.
class library:
    def __init__(self,books,book,borrowed_books):
        self.books = books
        books = []
        self.book = book
        borrowed_books = []
        self.borrowed_books = borrowed_books
    def display_l(self):
        print("We have :"+self.books)
    def borrow(self,book):
        book = str(input("What book would you like to borrow from the following: "+self.books))
        if book in self.books:
            print("you borrowed: " + book)
            self.books.remove(book)
            self.borrowed_books.append(book)
        else:
            print("That book isn't in our collection, sorry.")
    def Return(self,book):
        if book in self.books:
            print("you returned: " + self.borrowed_books)
            self.borrowed_books.remove(book)
            self.books.append(book)
        else:
            print("That book wasn't borrowed.")
    def display_b(self):
        print(self.borrowed_books)
    def update(self):
        while True:
            ans = input("Pls tell me what you want to do: Borrow book (borrow),Return books (return), Display Book that you have (display borrowed), and display book the library has(display library).")
            if ans == "borrow":
                book = str(input("what book do you want to borrow?"))
                library.borrow(book)
            elif ans == "return":
                yn = "y"
                while yn == "y":
                    book = input("what book do you want to return")
                    library.Return(book)
                    yn = str(input("any more?"))

            elif ans == "display borrowed":
                library.display_b()
            elif ans == "display library":
                library.display_l()
            else:
                print("thats not an instruction")
library1 = ["red","green","yellow","A study on how roses are red but violets arent blue"]
library2 = ["limon","lemon","orange","lime"]
library3 = ["hmmm","thoughts","'im confused'"," A regular book that is completely normal"]
library4 = ["rose","pink","supersaturated 4 dimensional green","Turquoise"]
Books = input("Which library do you use?(1,2,3,4)")
borrowed_books = []
l = library(Books,"None",borrowed_books)
l.update()