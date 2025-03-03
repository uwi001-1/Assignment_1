import book
import json

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        book = {"title": title, "author": author}
        self.books.append(book)
        return book 
     
    def view_books(self):
        str_str = json.dumps(self.books, indent=4)
        print(str_str)

    def search_title(self):
        try:
            python_list = json.loads(str_str)
        except:
            python_list = self.books
        target = input("Enter the title of the book to search: ")
        for i in range(len(python_list)):
            if python_list[i]["title"].lower() == target.lower():
                print("The book is in the list")
                print(python_list[i])
                break
            else:
                if i < len(python_list) -1:
                    continue
                else:
                    print("The book is not in the list")

library = Library()
library.add_book()
library.add_book()
library.view_books()
library.search_title()

