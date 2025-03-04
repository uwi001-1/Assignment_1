import library
import book

while True:
    action = input("Add/ View/ Search/ Update/ Delete/ Stop:  ").strip().lower()

    if action == "stop":
        library.take.save_books()
        print("STOPPED")
        break

    elif action == "add":
        library.take.add_book()
        library.take.save_books()
        print("ADDED")
    
    elif action == "view":
        print("VIEW")
        library.take.view_books()

    elif action == "search":
        print("SEARCH")
        library.take.search_title()
    
    elif action == "update":
        library.take.update_field()
        library.take.save_books()
        print("UPDATED")

    elif action == "delete":
        library.take.delete_book()
        library.take.save_books()
        print("DELETED")
    
    else:
        print("Invalid Input")