# new_list = []
# book = {}
# title = input("Enter the title of the book:")
# new_list.append(title)
# # author = input("Enter the author of the book:")
# # new_list[1] = author
# book["title"] = new_list[0]   

# print(book)
import json
import os  # To check if file exists

class Library:
    def __init__(self):
        self.books = self.load_books()  # Load existing books at startup

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        book = {"title": title, "author": author}  # Create book dictionary
        self.books.append(book)  # Add new book to the list
        self.save_books()  # Save after adding
        print("Book added successfully!")

    def save_books(self):
        with open("books.json", 'w') as file:  # Write the updated list to JSON
            json.dump(self.books, file, indent=4)
        print("Books saved successfully!")

    def load_books(self):
        if os.path.exists("books.json"):  # Check if file exists
            with open("books.json", "r") as file:
                try:
                    return json.load(file)  # Load existing books
                except json.JSONDecodeError:
                    print("Error: books.json is empty or corrupted. Resetting books.")
                    return []
        return []  # If file doesn't exist, return an empty list

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        str_str = json.dumps(self.books, indent=4)
        print(str_str)

# Create library instance and allow user to add/view books
library = Library()
library.add_book()
library.view_books()