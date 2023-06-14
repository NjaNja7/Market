from tkinter import *
from classes import Employee, Library, Book, library


class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='WELCOME TO THE LIBRARY', font='Times 40 bold', bg='lightblue',
              fg='red').pack(pady=250)


class Registration(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Registration', font='Times 20 bold', bg='lightblue',
              fg='red').pack(pady=10)
        Frame(self, height=2, relief=SUNKEN).pack(pady=10, fill=X)

        frame = Frame(self, bg='lightblue')
        frame.pack(pady=10)

        Label(frame, text='Full Name', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry1 = Entry(frame)
        entry1.pack()

        Label(frame, text='ID Number', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry2 = Entry(frame)
        entry2.pack()

        Label(frame, text='Phone Number', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry3 = Entry(frame)
        entry3.pack()

        Label(frame, text='Degree', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry4 = Entry(frame)
        entry4.pack()

        Label(frame, text='Username', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry5 = Entry(frame)
        entry5.pack()

        Label(frame, text='Password', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry6 = Entry(frame)
        entry6.pack()

        Button(frame, text='Register', bg='#D3DEDC', fg='black',
               command=lambda: register(entry1.get(), entry2.get(), entry3.get(),
                                        entry4.get(), entry5.get(), entry6.get())).pack(pady=10)

        label = Label(frame, font='Times 15 bold', bg='lightblue')
        label.pack(pady=10)

        def register(full_name, id_number, phone_number, degree, username, password):
            try:
                label.configure(text=library.register_employee(
                    Employee(full_name, id_number, phone_number, degree, username, password)))
            except:
                label.configure(text='Registration failed')


class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Login', font='Times 20 bold', bg='lightblue',
              fg='red').pack(pady=10)
        Frame(self, height=2, relief=SUNKEN).pack(pady=10, fill=X)

        frame = Frame(self, bg='lightblue')
        frame.pack(pady=110)

        Label(frame, text='Username', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry1 = Entry(frame)
        entry1.pack()
        Label(frame, text='Password', font='Times 15', bg='lightblue', fg='red').pack(pady=10)
        entry2 = Entry(frame)
        entry2.pack()

        Button(frame, text='Log in', bg='#D3DEDC', fg='black',
               command=lambda: login(entry1.get(), entry2.get())).pack(pady=40)

        label1 = Label(frame, font='Times 15 bold', bg='lightblue')
        label1.pack(pady=10)

        def login(username, password):
            try:
                label1.configure(text=library.login(username, password))
            except:
                label1.configure(text='Incorrect username or password.')


class IssueBook(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Issue Book', font='Times 20 bold', bg='lightblue',
              fg='red').pack(pady=10)
        Frame(self, height=2, relief=SUNKEN).pack(pady=10, fill=X)

        frame = Frame(self, bg='lightblue')
        frame.pack(pady=10)

        Label(frame, text='Title', font='Times 15', bg='lightblue', fg='red').pack(pady=10)
        entry1 = Entry(frame)
        entry1.pack(pady=10)

        book_info = Label(frame, bg='lightblue', fg='red')
        book_info.pack(pady=10)

        button1 = Button(frame, text='Find Book',
                         command=lambda: find(entry1.get()))
        button1.pack(pady=40)

        button2 = Button(frame, text='Issue Book',
                         command=lambda: issue(entry1.get()))
        button2.pack(pady=40)

        def find(title):
            try:
                book_info.configure(text=library.find_book(title))
            except:
                book_info.configure(text='The requested book was not found!')

        def issue(title):
            try:
                book_info.configure(text=library.issue_book(title))
            except:
                book_info.configure(text=f'{title} does not exist in the system, '
                                         f'please check the Title again.')


class ReturnBook(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Return Book', font='Times 20 bold', bg='lightblue',
              fg='red').pack(pady=10)
        Frame(self, height=2, relief=SUNKEN).pack(pady=10, fill=X)

        frame = Frame(self, bg='lightblue')
        frame.pack(pady=120)

        Label(frame, text='Title', font='Times 15', bg='lightblue', fg='red').pack(pady=10)
        entry1 = Entry(frame)
        entry1.pack()

        label = Label(frame, bg='lightblue', fg='red')
        label.pack(pady=10)

        Button(frame, text='Return Book',
               command=lambda: return_book(entry1.get())).pack(pady=30)

        def return_book(title):
            try:
                label.configure(text=library.return_book(title))
            except:
                label.configure(text=f'{title} has been returned to the system.')


class AddBook(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Add Book', font='Times 20 bold', bg='lightblue',
              fg='red').pack(pady=10)
        Frame(self, height=2, relief=SUNKEN).pack(pady=10, fill=X)

        frame = Frame(self, bg='lightblue')
        frame.pack(pady=10)

        Label(frame, text='Title', font='Times 15', bg='lightblue', fg='red').pack(pady=10)
        entry1 = Entry(frame)
        entry1.pack()

        Label(frame, text='Author', font='Times 15', bg='lightblue', fg='red').pack(pady=10)
        entry2 = Entry(frame)
        entry2.pack()

        Label(frame, text='ISBN', font='Times 15', bg='lightblue', fg='red').pack(pady=10)
        entry3 = Entry(frame)
        entry3.pack()

        label = Label(frame, bg='lightblue', fg='red')
        label.pack(pady=10)

        Button(frame, text='Add Book',
               command=lambda: add_book(entry1.get(), entry2.get(), entry3.get())).pack(pady=30)

        def add_book(title, author, isbn):
            try:
                label.configure(text=library.add_book(title, author, isbn))
            except:
                label.configure(text=f'{title} by {author} has been added to the system.')


class RemoveBook(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Remove Book', font='Times 15 bold', bg='lightblue',
              fg='red').pack(pady=10)
        Frame(self, height=2, relief=SUNKEN).pack(pady=10, fill=X)

        frame = Frame(self, bg='lightblue')
        frame.pack(pady=120)

        Label(frame, text='Title:', font='Comic 15', bg='lightblue', fg='red').pack(pady=10)
        entry = Entry(frame)
        entry.pack(pady=10)

        Button(frame, text='Remove Book',
               command=lambda: remove(entry.get())).pack(pady=20)

        label = Label(frame, bg='lightblue', fg='red')
        label.pack(pady=10)

        def remove(title):
            try:
                label.configure(text=library.remove_book(title))
            except:
                label.configure(text=f'The book {title} does not exist in the system, please check the Title again.')


class Hire(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Hire', font='Times 20 bold', bg='lightblue',
              fg='red').pack(pady=10)
        Frame(self, height=2, relief=SUNKEN).pack(pady=10, fill=X)

        frame = Frame(self, bg='lightblue')
        frame.pack(pady=10)

        Label(frame, text='Name and Surname:', font='Times 15', bg='lightblue', fg='red').pack(pady=5)
        entry1 = Entry(frame)
        entry1.pack(pady=5)

        Label(frame, text='ID Number:', font='Times 15', bg='lightblue', fg='red').pack(pady=5)
        entry2 = Entry(frame)
        entry2.pack(pady=5)

        Label(frame, text='Phone Number:', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry3 = Entry(frame)
        entry3.pack()

        Label(frame, text='Degree:', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry4 = Entry(frame)
        entry4.pack()

        Label(frame, text='Username:', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry5 = Entry(frame)
        entry5.pack(anchor=CENTER)

        Label(frame, text='Password:', font='Times 15', bg='lightblue',
              fg='red').pack(pady=10)
        entry6 = Entry(frame)
        entry6.pack()

        Button(frame, text='Hire', command=lambda:
        manager_hire(entry1.get(), entry2.get(),
                    entry3.get(), entry4.get(), entry5.get(), entry6.get())).pack(pady=10)

        label = Label(frame, bg='lightblue', fg='red')
        label.pack(pady=10)

        def manager_hire(name_surname, id_number, phone_number, degree, username, password):
            try:
                label.configure(text=library.hire(
                    Employee(name_surname, id_number, phone_number, degree, username, password)))
            except:
                label.configure(text='Failed to hire a new employee.')


class Fire(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Fire', font='Times 20 bold', bg='lightblue',
              fg='red').pack(pady=10)
        Frame(self, height=2, relief=SUNKEN).pack(pady=10, fill=X)

        frame = Frame(self, bg='lightblue')
        frame.pack(pady=140)

        Label(frame, text='Name and Surname:', font='Times 15', bg='lightblue', fg='red').pack(pady=5)
        entry1 = Entry(frame)
        entry1.pack(pady=5)

        Button(frame, text='Fire', command=lambda: fire(entry1.get())).pack(pady=10)

        label = Label(frame, bg='lightblue', fg='red')
        label.pack(pady=10)

        def fire(name_surname):
            try:
                label.configure(text=library.fire(name_surname))
            except:
                label.configure(text=f'{name_surname} does not exist in the system.')


pages = (HomePage, Registration, Login, IssueBook, ReturnBook,
         AddBook, RemoveBook, Hire, Fire)
