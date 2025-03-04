import book
import json
import os

class Library:
    def __init__(self):
        self.books = self.load_books()  #loads existing books at the beginning
    
    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")
        Isbn = input("Enter the ISBN of the book: ")
        #create dictionary 
        book = {"Title": title, "Author": author, "Genre": genre, "ISBN": Isbn}
        #adding the dictionary to the list 
        self.books.append(book)
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
            str_str = json.dumps(self.books, indent=4)
            print(str_str)
        else:
            print("No books available")
            return
        
    def find_target(self):
        try:
            python_list = json.loads(str_str)
        except:      #if not in JSON string
            python_list = self.books
        target = input("Enter the title of the book: ").strip().lower()
        return python_list, target

    def search_title(self):
        python_list, target = self.find_target()
        for i in range(len(python_list)):
            if python_list[i]["Title"].lower() == target:
                print("The book is in the list")
                print(python_list[i])
                break
            else:
                if i < len(python_list) -1:
                    continue
                else:
                    print("The book is not in the list")

    def update_field(self):
        python_list, target = self.find_target()
        for i in range(len(python_list)):
            if python_list[i]["Title"].lower() == target:
                print("The book is in the list")
                update = input("Enter which field you want to update:  ")   #if enter new field, it will add it as well
                change = input("Enter what you want to change in that field:  ")   #value of the field
                python_list[i][update] = change
                break
            else:
                if i < len(python_list) -1:
                    continue
                else:
                    print("The book is not in the list")

    def delete_book(self):
        python_list, target = self.find_target()
        for i in range(len(python_list)):
            if python_list[i]["Title"].lower() == target:
                print("The book is in the list")
                # chose = input("Enter field you want to delete:  ").strip().lower()
                del python_list[i]
                break
            else:
                if i < len(python_list) -1:
                    continue
                else:
                    print("The book is not in the list")

take = Library()