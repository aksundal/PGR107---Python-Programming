# -*- coding: utf-8 -*-

# Book class

class Book:
    def __init__(self, title, author, num_pages): # to store information 
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.checked_out = False # False so that we can use checked in later!

    def __str__(self):
        status = "Available" if not self.checked_out else "Checked out" # checks if self.checked out if false becomes available, if true becomes checked out 
        return f"{self.title} by {self.author} ({self.num_pages} pages) — {status}" #puts the books info together 

# Library class 
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book): #defines the way to add book
        self.books.append(book)
        print(f"The book is added: {book.title}") 

    def remove_book(self, title): # remove a book by the title (the string), not by the bject
        for book in self.books: # loop 
            if book.title == title:
                self.books.remove(book)
                print(f"The book is removed: {title}") # Deletes the book from the object list
                return
        print(f"We can't remove – there is no book called {title}") # runs in case the loop finsihes and warns that no such title exist 

    def check_out(self, title): # how check out works, borrow the book and mark it checked out
        for book in self.books:  # loop to find the book
            if book.title == title: # is it the right book? 
                if not book.checked_out:
                    book.checked_out = True 
                    print(f" Checked out: {title}") # if found and its not borrowed then true 
                else:
                    print(f" Already checked out: {title}") # if it is borrowed prints to warn you 
                return # stop the loop once its found
        print(f" The book can't be checked out – there is no book called {title}") # if not print out this 

    def check_in(self, title): 
        for book in self.books: # same loop pattern 
            if book.title == title:
                if book.checked_out:
                    book.checked_out = False
                    print(f" Returned: {title}")
                else:
                    print(f" That book wasn’t checked out: {title}")
                return
        print(f" We can't return – there is no book called {title}")

    def list_books(self):
        print("\n The Library now has:") # to show what the library has
        if not self.books:
            print("   (nothing!)")
        for book in self.books: # If self.book is empty then it will rint nothing!
            
            print(f"  - {book}")
        print()


def main():
    lib = Library() # the container for all the book tests
    book1 = Book("The Alchemist", "Paulo Coelho", 208) # the library 
    book2 = Book("A Court of Thorns and Roses", "Sarah J. Maas", 448)
    book3 = Book("The Song of Achilles", "Madeline Miller", 368)

    lib.add_book(book1) # make three books for the library that runs Book._init_
    lib.add_book(book2)
    lib.add_book(book3)
    lib.list_books() # adds the books

    lib.check_out("The Alchemist")
    lib.check_out("The Alchemist")       # try again if the book is not found
    lib.check_in("The Alchemist")
    lib.check_in("Black Panther")            # change to whatever book that is not in the lib.add_book

    lib.remove_book("The Song of Achilles")
    lib.remove_book("Batman vs Superman")    # random book that is not in the library 
    lib.list_books() #one is true the other is false and prints it ut 


if __name__ == "__main__": # prints out whatever is left 
    main()
