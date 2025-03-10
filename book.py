class Book:
    def __init__(self, title, author, genre, Isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.ISBN = Isbn
        
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ISBN: {self.ISBN}"  