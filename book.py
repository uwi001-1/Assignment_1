class Book:
    def __init__(self, title, author, year, Isbn, price):
        self.title = title
        self.author = author
        self.year = year
        self.ISBN = Isbn
        self.price = price
        
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.ISBN}, Price: {self.price}"
    