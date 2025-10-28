

class Book:
    def __init__(self,title,author,isbn,available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def __str__(self):
        return f'{self.title}'
    
    def __repr__(self):
        return self.__str__()


    def display_info(self):
        print(f'The book {self.title} written by {self.author}.\nISBN: {self.isbn} . Available copies: {self.available_copies}')

    def borrow(self):
        if self.available_copies>0:
            self.available_copies-=1
            print(f'Successfully borrowed a book. \nCopies left:{self.available_copies}')
    
    def return_book(self):
        self.available_copies+=1
        print(f'Increased  copies \nCopies left:{self.available_copies}')

# book object created
book1 = Book('Alchemist','Paulo Coelo',123,10)  
book2 = Book('Atomic Habit','James Clear',345,25)  


# borrow_book(book) → adds book to borrowed_books if available
# return_book(book) → removes book from list and returns it

class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self,book):
        self.borrowed_books.append(book)
        print(self.borrowed_books)

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else

memb1 = Member('Arun',67273)
memb1.borrow_book(book1)
memb1.borrow_book(book2)
memb1.return_book('book1')
print(memb1.borrowed_books)
# print(book1)