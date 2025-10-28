# Task: Library Management System (Console-Based)

class Book:
    def __init__(self,title,author,isbn,available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        status = 'Available' if self.available else 'Not Available'
        return f'{self.title} by {self.author} || {self.isbn} | {status}'
    

class User:
    def __init__(self,name,user_id,borrowed_books):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books

    def borrow_book(self,book):
        book.available = False

    def return_book(self,book):
        book.available = True

class Library:
    def __init__(self):
        self.books = []
        self.user = []
    

    def add_book(self):
        pass

    def remove_book(self):
        pass

    def find_book(self):
        pass

    def show_available_books(self):
        pass