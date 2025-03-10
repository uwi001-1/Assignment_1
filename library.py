import book
import json
import os

class Library:
    def __init__(self):
        self.books = self.load_books()  #loads existing books at the beginning
        self.book_id = self.get_next_id()     #initialize book ID
    
    def get_next_id(self):
        if self.books:    #checks if there are any books in the list
            return max(book["ID"] for book in self.books) + 1  #max helps find the highest ID
        return 1    #if no books, then start from 1

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")
        Isbn = input("Enter the ISBN of the book: ")
        #create dictionary 
        book = {
            "ID": self.book_id,
            "Title": title, 
            "Author": author, 
            "Genre": genre, 
            "ISBN": Isbn
        }
        #adding the dictionary to the list 
        self.books.append(book)
        self.book_id += 1     #increment the ID
        self.save_books()     #save to file after adding

    def save_books(self):
        with open("books.json", 'w') as file:     #writes the updated list to JSON
            json.dump(self.books, file, indent=4)
     
    def load_books(self):
        if os.path.exists("books.json"):   #checks if the file exists
            with open("books.json", "r") as f:
                try:
                    return json.load(f)   #read JSON file and convert into Python object
                except json.JSONDecodeError:
                    print("Error empty list")
                    return [] #return empty list, if there is error
        return []    #return empty list, if file doesn't exist
    
    def view_books(self):
        if self.books:
            str_str = json.dumps(self.books, indent=4)  #to view the list in the JSON string method
            print(str_str)
        else:
            print("No books available")    #if the list is empty
            return
        
    def find_target(self):
        try:    #if in JSON string, convert to list
            python_list = json.loads(str_str)
        except:      #if not in JSON string
            python_list = self.books 
        target = input("Enter the title of the book: ").strip().lower()
        return python_list, target

    def search_title(self):
        python_list, target = self.find_target()  # Get book list and target title
        found_books = []  # List to store matching books

        for book in python_list:
            if book["Title"].lower() == target:  # Compare title's value to target
                found_books.append(book)  # Store matching books

        if found_books:
            print("The book is in the list")  # Print only once
            for book in found_books:
                print(book)  # Print each matching book
        else:
            print("The book is not in the list")  # If no book matches

    def update_field(self):
        python_list, target = self.find_target()
        found_books = []
        
        for i, book in enumerate(python_list):
            if book["Title"].lower() == target:
                found_books.append((i,book))

        if not found_books:
            print("The book is not in the list")
            return
                
                #Show all matching books
        print(f"Found {len(found_books)} book(s) with the title '{target}':")
        #i---actual index of python_list       book is dictionary
        for ab, (i, book) in enumerate(found_books, start=1):
            print(f"{ab}. {book}")  # Numbered list for user choice
                
        while True:
            try:
                choice = int(input("Enter the number of the book you want to update: ")) - 1
                if 0 <= choice and choice < len(found_books): 
                    update = input("Enter which field you want to update:  ").strip()
                    
                    if update == "ID":     #prevent ID from being updated
                        print("You cannot update the ID field!")
                        continue   

                    if update in book:
                        change = input(f"Enter the new value for {update}: ").strip()  #value of the field
                        book[update] = change
                        return
                    else:
                        print("Invalid Field! Enter existing field.")
                else:
                    print("Invalid choice. PLease enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number")   

    def delete_book(self):
        python_list, target = self.find_target()
        found_books = []  # List to store matching books

        for i, book in enumerate(python_list):  #Loop through books with index
            if book["Title"].lower() == target:
                found_books.append((i, book))  #Store index and book data

        if not found_books:
            print("The book is not in the list")
            return  # Exit function if no books found
        #Show all matching books
        print(f"Found {len(found_books)} book(s) with the title '{target}':")
        #i---actual index of python_list       book is dictionary
        for ab, (i, book) in enumerate(found_books, start=1):
            print(f"{ab}. {book}")  # Numbered list for user choice

        #Choose which book to delete
        while True:
            try:
                choice = int(input("Enter the number of the book you want to delete: ")) - 1
                if 0 <= choice and choice < len(found_books):      #Ensure valid choice
                    del python_list[found_books[choice][0]]        #Delete selected book
                    #choice--found_books' index   and 0--python_list's index 
                    print("DELETED THE BOOK")
                    return 
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

take = Library()
