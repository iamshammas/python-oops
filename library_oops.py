from abc import abstractmethod,ABC

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

@abstractmethod
class LibraryUser(ABC):
    def borrow_book(self):
        pass

    def return_book(self):
        pass

class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id = member_id
        self._borrowed_books = []

    def borrow_book(self,book):
        self._borrowed_books.append(book)
        # print(self.__borrowed_books)

    def get_book(self):
        return self._borrowed_books

    def return_book(self,book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
        else:
            print('There is no book with the given name')

memb1 = Member('Arun',67273)
memb1.borrow_book(book1)
memb1.borrow_book(book2)
memb1.return_book(book1)
# print(memb1.__borrowed_books)

# Class: StudentMember and TeacherMember (Derived Classes)
# Students can borrow up to 3 books
# Teachers can borrow up to 5 books
# Override borrow_book() to enforce these limits

class StudentMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        
    # def show(self):
    #     print(f'borrowed {countt}')


    def borrow_book(self, book):
        if len(self._borrowed_books)>=3:
            print('Student can only borrow upto 3 books at a time')
            # print(len(self.borrowed_books))
        else:
            self._borrowed_books.append(book)
            # print(len(self.borrowed_books))
            
        # print(len(self.borrowed_books))

    def return_book(self, book):
        self.__borrowed_books.remove(book)
        print('successfully returned')
    

class TeacherMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)

    def borrow_book(self, book):
        if len(self._borrowed_books)>=5:
            print('Student can only borrow upto 5 books at a time')
        else:
            self._borrowed_books.append(book)

stud = StudentMember('Rahul',887832)
teach = TeacherMember('Shanmugam',89344)
stud.borrow_book('Hell giys')
stud.borrow_book('book number two')
stud.borrow_book('third book griys')
stud.borrow_book('fourth book griys')
# stud.return_book('book number two')
# print(stud.borrowed_books)

## adding teacher's book
teach.borrow_book("teacher's book 1")
teach.borrow_book("teacher's book 2")
teach.borrow_book("teacher's book 3")

teach.return_book("teacher's book 1")

# print(teach.borrowed_books)

print(teach.get_book())
print(stud.get_book())

# 5. **Polymorphism**
    # - Show that `StudentMember` and `TeacherMember` behave differently when borrowing books, but are used interchangeably through a reference of type `LibraryUser`.

