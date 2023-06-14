from pages import *

global pages


class GUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('Library')
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.display_pages = {}

        menu = Menu(container)
        employees_menu = Menu(menu, tearoff=0)
        employees_menu.add_command(label='Register', command=lambda: self.show_page(Registration))
        employees_menu.add_command(label='Login', command=lambda: self.show_page(Login))
        employees_menu.add_separator()
        employees_menu.add_command(label='Hire', command=lambda: self.check_manager(Hire))
        employees_menu.add_command(label='Fire', command=lambda: self.check_manager(Fire))
        employees_menu.add_separator()
        employees_menu.add_command(label='Exit', command=lambda: self.destroy())

        menu.add_cascade(label='Employees', menu=employees_menu)

        books_menu = Menu(menu, tearoff=0)
        books_menu.add_command(label='Issue Book', command=lambda: self.check(IssueBook))
        books_menu.add_command(label='Return Book', command=lambda: self.check(ReturnBook))
        books_menu.add_separator()
        books_menu.add_command(label='Add Book', command=lambda: self.check(AddBook))
        books_menu.add_command(label='Remove Book', command=lambda: self.check(RemoveBook))

        menu.add_cascade(label='Books', menu=books_menu)

        Tk.config(self, menu=menu)

        for page in pages:
            page_instance = page(container, self)
            self.display_pages[page] = page_instance
            page_instance.grid(row=0, column=0, sticky='news')

        self.show_page(HomePage)

    def show_page(self, controller):
        page_instance = self.display_pages[controller]
        page_instance.tkraise()

    def check(self, controller):
        if library.is_logged_in:
            self.show_page(controller)
        else:
            self.show_page(Login)

    def check_manager(self, controller):
        for employee in library.employees:
            if employee.manager:
                self.show_page(controller)
            else:
                self.show_page(Login)


LIBRARY = GUI()
LIBRARY.geometry('1200x600')
LIBRARY.mainloop()
