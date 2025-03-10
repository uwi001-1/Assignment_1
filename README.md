# Assignment_2
### Overall Structure 

# Personal Library Management System
A simple Python-based command-line **Personal Library Management System** that allows users to manage their book collection. This system supports features such as adding, viewing, searching, updating, and deleting books from the library.

## Features
- **Add Books**: Add new books to the library by providing details like title, author, genre, and ISBN.
- **View Books**: View the complete list of books currently in the library.
- **Search Books**: Search for books by title.
- **Update Book Details**: Update the details of a specific book, except for the ID.
- **Delete Books**: Delete a book from the library by searching for its title.
- **Data Persistence**: All books are stored in a **JSON** file, ensuring data is saved between sessions.

### books.json: The file that stores the book data in JSON format.

## Error Handling
The system includes basic error handling for:
- Invalid user input.
- Empty or corrupted JSON files.
- Non-existent files.