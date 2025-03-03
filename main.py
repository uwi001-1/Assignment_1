import library
import book

while True:
    action = input("Add/ View/ Search/ Update/ Delete/ Stop:  ").strip().lower()

    if action == "stop":
        print("STOPPED")
        break

    elif action == "add":
        library.take.add_book()
        print("ADDED")
    
    elif action == "view":
        print("VIEW")
        library.take.view_books()

    elif action == "search":
        print("SEARCH")
        library.take.search_title()
    
    elif action == "update":
        library.take.update_field()
        print("UPDATED")

    elif action == "delete":
        print("DELETED")
    
    else:
        print("Invalid Input")