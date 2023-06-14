class Employee:
    def __init__(self, full_name, id_number, phone_number, degree, username, password, manager=False):
        Employee.validation(full_name, id_number, phone_number, degree, username, password)
        self.full_name = full_name
        self.id_number = id_number
        self.phone_number = phone_number
        self.degree = degree
        self.username = username
        self.password = password
        self.manager = manager

    def __str__(self):
        return f'Employee: {self.full_name}\nID Number: {self.id_number}\nPhone Number: ' \
               f'{self.phone_number}\n'

    @staticmethod
    def validation(full_name, id_number, phone_number, degree, username, password):
        assert type(full_name) == str, 'Must be a string'
        assert type(id_number) == str, 'Must be a string'
        assert type(phone_number) == str, 'Must be a string'
        assert type(degree) == str, 'Must be a string'
        assert type(username) == str, 'Must be a string'
        assert type(password) == str, 'Must be a string'
        # assert type(manager) == , 'Must be True or False'


class Book:
    def __init__(self, title, author, publishing_year, country_of_origin, language):
        Book.validation(title, author, publishing_year, country_of_origin, language)
        self.title = title
        self.author = author
        self.publishing_year = publishing_year
        self.country_of_origin = country_of_origin
        self.language = language
        self.status = 'In stock'

    def __str__(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nCountry of Origin: {self.country_of_origin}\n' \
               f'Original Language: {self.language}\nStatus: {self.status}\n'

    @staticmethod
    def validation(title, author, publishing_year, country_of_origin, language):
        assert type(title) == str, 'Must be a string'
        assert type(author) == str, 'Must be a string'
        assert type(publishing_year) == str, 'Must be a string'
        assert type(country_of_origin) == str, 'Must be a string'
        assert type(language) == str, 'Must be a string'
        # assert type(status) == str, 'Must be a string'


class Library:
    def __init__(self, employees=[], books=[]):
        Library.validation(employees, books)
        self.employees = employees
        self.books = books
        self.is_logged_in = False

    @staticmethod
    def validation(employees, books):
        assert type(employees) == list, 'Must be a list of employees'
        assert type(books) == list, 'Must be a list of books'
        for emp in employees:
            assert type(emp) == Employee, 'All elements must be objects of the Employee class.'
        for bk in books:
            assert type(bk) == Book, 'All elements must be objects of the Book class.'

    def register_employee(self, employee):
        assert type(employee) == Employee, 'Must be an object of the Employee class'
        self.employees.append(employee)
        return f'Welcome, {employee.full_name}.'

    def login(self, username, password):
        for employee in self.employees:
            if employee.username == username and employee.password == password:
                self.is_logged_in = True
                return f'Welcome, {employee.full_name}, to the library system.'
        else:
            raise Exception

    def add_book(self, book):
        assert type(book) == Book, 'Must be an object of the Book class.'
        self.books.append(book)
        return f'{book.title} has been added.'

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f'{title} has been removed.'
        else:
            raise Exception

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return f'Title: {book.title}\nAuthor: {book.author}\nCountry of Origin: {book.country_of_origin}\n' \
                       f'Original Language: {book.language}\nStatus: {book.status}\n'
        else:
            raise Exception

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.status == 'In stock':
                book.status = 'Issued'
                return f'{title} has been issued.'
        else:
            raise Exception

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.status == 'Issued':
                book.status = 'In stock'
                return f'{title} has been returned.'
        else:
            raise Exception

    def hire_employee(self, new_employee):
        assert type(new_employee) == Employee, 'The object must be an instance of the Employee class.'
        self.employees.append(new_employee)
        return f'{new_employee.full_name} has been hired.'

    def dismiss_employee(self, full_name):
        for employee in self.employees:
            if employee.full_name == full_name:
                self.employees.remove(employee)
                return f'{full_name} has been dismissed.'
        else:
            raise Exception


books = [l.strip().split('-') for l in open('books.txt')]

book_list = []

for book in books:
    book_list.append(Book(book[0], book[1], book[2], book[3], book[4]))

# print(book_list)

employees = [l.strip().split('-') for l in open('employees.txt')]

employee_list = []

for employee in employees:
    employee_list.append(Employee(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5], employee[6]))

# print(employee_list)

library = Library(employee_list, book_list)
