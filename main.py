import library
import book

while True:
    try:
        action = int(input("Add/ View/ Search/ Update/ Delete/ Stop (in numbers):  "))
        if action == 6:
            library.take.save_books()
            print("THE PROGRAM IS STOPPED")
            break

        elif action == 1:
            library.take.add_book()
            library.take.save_books()
            print("BOOK IS ADDED")
    
        elif action == 2:
            print("VIEW THE LIBRARY")
            library.take.view_books()

        elif action == 3:
            print("SEARCH IN THE LIBRARY")
            library.take.search_title()
    
        elif action == 4:
            library.take.update_field()
            library.take.save_books()
            print("UPDATED THE FIELD OF THE BOOK")

        elif action == 5:
            library.take.delete_book()
            library.take.save_books()
    
        else:
            print("Invalid Input")
    except ValueError:
        print("Invalid Input. Enter a number.")