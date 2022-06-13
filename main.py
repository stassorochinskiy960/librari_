import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.init_main_2()
        self.init_main_5()
        # --------------------
        self.tollbar()
        self.db = db
        # --------------------
        self.view_records()
        self.view_records_2()
        self.view_records_5()

    def tollbar(self):
        # create toolbar for save vidjets
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # add buttons and some on toolbar
        btn_open_dialog = tk.Button(toolbar, text='додати', command=self.open_dialog, bg='#EB2E2E', bd=2,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)
        # add buttons and some on toolbar
        btn_update_dialog = tk.Button(toolbar, text='редагувати', command=self.open_update_dialog, bg='#18DEF2', bd=2,
                                    compound=tk.TOP)
        btn_update_dialog.pack(side=tk.LEFT)
        # add buttons and some on toolbar
        btn_delet_dialog = tk.Button(toolbar, text='видалити', command=self.delet, bg='#9BABD4', bd=2,
                                      compound=tk.TOP)
        btn_delet_dialog.pack(side=tk.LEFT)

        btn_search = tk.Button(toolbar, text='Поиск', bg='#B4F6F0', bd=2, compound=tk.TOP,
                               command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#F6A50F', bd=2, compound=tk.TOP,
                                command=self.update)
        btn_refresh.pack(side=tk.LEFT)

    def update(self):
        self.view_records()
        self.view_records_2()
        self.view_records_5()

    def delet(self):
        self.delete_rekords()
        self.delete_rekords_2()
        self.delete_rekords_5()

    def init_main(self):
        # add tree or table on main root
        self.tree_book = ttk.Treeview(self, columns=('id', 'назва', 'автор', 'жанр', 'ціна'),
                                      height=15, show='headings')
        # orientation colums tree_book
        self.tree_book.column('id', width=50, anchor=tk.CENTER)
        self.tree_book.column('назва', width=250, anchor=tk.CENTER)
        self.tree_book.column('автор', width=70, anchor=tk.CENTER)
        self.tree_book.column('жанр', width=70, anchor=tk.CENTER)
        self.tree_book.column('ціна', width=70, anchor=tk.CENTER)
        # name colum tree_book
        self.tree_book.heading('id', text='id')
        self.tree_book.heading('назва', text='назва')
        self.tree_book.heading('автор', text='імя автору')
        self.tree_book.heading('жанр', text='назва жанру')
        self.tree_book.heading('ціна', text='ціна')
        # view vidjests
        self.tree_book.pack(side=tk.BOTTOM)

        '''# add button for close children root
        button_cansel = ttk.Button(self, text='закрити', command=self.destroy)
        button_cansel.pack(side=tk.LEFT)'''

    def init_main_2(self):
        # add tree or table on main root
        self.tree_readers = ttk.Treeview(self, columns=('id_r', 'фіо', 'телефон'), height=15, show='headings')
        # orientation colums tree_readers
        self.tree_readers.column('id_r', width=50, anchor=tk.CENTER)
        self.tree_readers.column('фіо', width=230, anchor=tk.CENTER)
        self.tree_readers.column('телефон', width=120, anchor=tk.CENTER)
        # name colum tree_readers
        self.tree_readers.heading('id_r', text='id')
        self.tree_readers.heading('фіо', text='фіо')
        self.tree_readers.heading('телефон', text='телефон')
        # view vidjests
        self.tree_readers.pack(side=tk.LEFT)

        '''# add button for close children root
        button_cansel = ttk.Button(self, text='закрити', command=self.destroy)
        button_cansel.pack(side=tk.LEFT)'''

    def init_main_5(self):  # видача книг
        # add tree or table on main root
        self.tree_give_book = ttk.Treeview(self, columns=('id_g_b', 'id_b', 'id_r', 'data'), height=15, show='headings')
        # orientation columns tree_avtor
        self.tree_give_book.column('id_g_b', width=50, anchor=tk.CENTER)
        self.tree_give_book.column('id_b', width=70, anchor=tk.CENTER)
        self.tree_give_book.column('id_r', width=70, anchor=tk.CENTER)
        self.tree_give_book.column('data', width=100, anchor=tk.CENTER)
        # name colum tree_janr
        self.tree_give_book.heading('id_g_b', text='id')
        self.tree_give_book.heading('id_b', text="id книги")
        self.tree_give_book.heading('id_r', text="id читача")
        self.tree_give_book.heading('data', text='дата')
        # view vidjests
        self.tree_give_book.pack(side=tk.RIGHT)

    # create function for add data in database table книги
    def records(self, nazva, avtor, janor, cina):  # connect method insert_data class's DB() how var db
        self.db.insert_data(nazva, avtor, janor, cina)
        self.view_records()

    def update_records(self, nazva, avtor, janor, cina):
        self.db.c.execute('''UPDATE книги SET название=?, автор=?, жанр=?, стоимость=? WHERE кодКниги=?''',
                          (nazva, avtor, janor, cina, self.tree_book.set(self.tree_book.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM книги''')
        [self.tree_book.delete(i) for i in self.tree_book.get_children()]
        [self.tree_book.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    # create function for add data in database table читатели
    def records_2(self, fio, tell):
        self.db.insert_data_2(fio, tell)
        self.view_records_2()

    def update_records_2(self, fio, tell):
        self.db.c.execute('''UPDATE читатели SET ФИО=?, телефон=? WHERE кодЧитателя=?''',
                          (fio, tell, self.tree_readers.set(self.tree_readers.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records_2()

    def view_records_2(self):
        self.db.c.execute('''SELECT * FROM читатели''')
        [self.tree_readers.delete(i) for i in self.tree_readers.get_children()]
        [self.tree_readers.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    # create function for add data in database table
    def records_5(self, book, reader, given):
        self.db.insert_data_5(book, reader, given)
        self.view_records_5()

    def update_records_5(self, book, reader, given):
        self.db.c.execute('''UPDATE видача_Книг SET кодКниги=?, кодЧитателя=?, датаВыдачи=? WHERE кодВыдачи=?''',
                          (book, reader, given, self.tree_give_book.set(self.tree_give_book.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records_5()


    def view_records_5(self):
        self.db.c.execute('''SELECT * FROM видача_Книг''')
        [self.tree_give_book.delete(i) for i in self.tree_give_book.get_children()]
        [self.tree_give_book.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_rekords(self):
        for selection_item in self.tree_book.selection():
            self.db.c.execute('''DELETE FROM книги WHERE кодКниги=? ''', (self.tree_book.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def delete_rekords_2(self):
        for selection_item in self.tree_readers.selection():
            self.db.c.execute('''DELETE FROM читатели WHERE кодЧитателя=? ''', (self.tree_readers.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records_2()

    def delete_rekords_5(self):
        for selection_item in self.tree_give_book.selection():
            self.db.c.execute('''DELETE FROM видача_Книг WHERE кодВыдачи=? ''', (self.tree_give_book.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records_5()

    def search_records(self, nazva):
        nazva = ('%' + nazva + '%',)
        self.db.c.execute('''SELECT * FROM книги WHERE название LIKE ?''', nazva)
        [self.tree_book.delete(i) for i in self.tree_book.get_children()]
        [self.tree_book.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def search_records_2(self, fio):
        fio = ('%' + fio + '%',)
        self.db.c.execute('''SELECT * FROM читатели WHERE ФИО LIKE ?''', fio)
        [self.tree_readers.delete(i) for i in self.tree_readers.get_children()]
        [self.tree_readers.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def search_records_5(self, given):
        given = ('%' + given + '%',)
        self.db.c.execute('''SELECT * FROM видача_Книг WHERE датаВыдачи LIKE ?''', given)
        [self.tree_give_book.delete(i) for i in self.tree_give_book.get_children()]
        [self.tree_give_book.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    # call child class for start child root
    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app  # this connecting method records class's Main()

    # create child root who start due to main root
    def init_child(self):
        self.title("додати інформацію")
        self.geometry('650x500+300+100')
        # self.resizable(False, False)

        # inscription(label) for input for data in tree_book or all table
        label_nazva = tk.Label(self, text='назва')
        label_nazva.place(x=50, y=50)
        label_avtor = tk.Label(self, text='імя автору')
        label_avtor.place(x=50, y=80)
        label_janor = tk.Label(self, text='назва жанру')
        label_janor.place(x=50, y=110)
        label_cina = tk.Label(self, text='ціна')
        label_cina.place(x=50, y=140)
        # add inputs fields
        label_fio = tk.Label(self, text='ФІО')
        label_fio.place(x=50, y=170)
        label_tell = tk.Label(self, text='телефон')
        label_tell.place(x=50, y=200)
        # add inputs fields
        label_book = tk.Label(self, text='id книги')
        label_book.place(x=50, y=230)
        label_reader = tk.Label(self, text='id читача')
        label_reader.place(x=50, y=260)
        label_given = tk.Label(self, text='дата видачі')
        label_given.place(x=50, y=290)



        # field for input data in tree_book or all table
        self.entry_nazva = ttk.Entry(self)
        self.entry_nazva.place(x=200, y=50)
        self.entry_avtor = ttk.Entry(self)
        self.entry_avtor.place(x=200, y=80)
        self.entry_janor = ttk.Entry(self)
        self.entry_janor.place(x=200, y=110)
        self.entry_cina = ttk.Entry(self)
        self.entry_cina.place(x=200, y=140)
        # add inputs fields 2
        self.entry_fio = ttk.Entry(self)
        self.entry_fio.place(x=200, y=170)
        self.entry_tell = ttk.Entry(self)
        self.entry_tell.place(x=200, y=200)
        # add inputs fields 5
        self.entry_book = ttk.Entry(self)
        self.entry_book.place(x=200, y=230)
        self.entry_reader = ttk.Entry(self)
        self.entry_reader.place(x=200, y=260)
        self.entry_given = ttk.Entry(self)
        self.entry_given.place(x=200, y=290)

        # add button for close children root
        button_cansel = ttk.Button(self, text='закрити', command=self.destroy)
        button_cansel.place(x=560, y=300)
        # add button add-ok
        self.button_add = ttk.Button(self, text='додати у книги')
        self.button_add.place(x=400, y=300)
        self.button_add.bind('<Button-1>', lambda event: self.view.records(self.entry_nazva.get(), self.entry_avtor.get(),
                                                                           self.entry_janor.get(), self.entry_cina.get()))
        # add button add-ok
        self.button_add_2 = ttk.Button(self, text='додати в читачі')
        self.button_add_2.place(x=400, y=330)
        self.button_add_2.bind('<Button-1>', lambda event: self.view.records_2(self.entry_fio.get(), self.entry_tell.get()))
        # add button add-ok
        self.button_add_5 = ttk.Button(self, text='додати в "видача книг"')
        self.button_add_5.place(x=400, y=360)
        self.button_add_5.bind('<Button-1>', lambda event: self.view.records_5(self.entry_book.get(),
                                                                               self.entry_reader.get(),
                                                                               self.entry_given.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title('Редагувати')
        btn_edit = ttk.Button(self, text='Редагувати таблицю книги')
        btn_edit.place(x=400, y=300)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_records(self.entry_nazva.get(), self.entry_avtor.get(),
                                                                           self.entry_janor.get(), self.entry_cina.get()))

        btn_edit_2 = ttk.Button(self, text='Редагувати таблицю читачі')
        btn_edit_2.place(x=400, y=330)
        btn_edit_2.bind('<Button-1>', lambda event: self.view.update_records_2(self.entry_fio.get(), self.entry_tell.get()))

        btn_edit_5 = ttk.Button(self, text='Редагувати таблицю видача книг')
        btn_edit_5.place(x=400, y=360)
        btn_edit_5.bind('<Button-1>', lambda event: self.view.update_records_5(self.entry_book.get(),
                                                                               self.entry_reader.get(),
                                                                               self.entry_given.get()))
        self.button_add.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('пошук')
        self.geometry('350x250+400+300')
        self.resizable(False, False)

        lbl_search = tk.Label(self, text='Поиск в книгаг')
        lbl_search.place(x=10, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=115, y=20, width=150)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        lbl_search_2 = tk.Label(self, text='Поиск в читачах')
        lbl_search_2.place(x=10, y=80)

        self.entry_search_2 = ttk.Entry(self)
        self.entry_search_2.place(x=115, y=80, width=150)

        btn_search_2 = ttk.Button(self, text='Поиск')
        btn_search_2.place(x=105, y=110)
        btn_search_2.bind('<Button-1>', lambda event: self.view.search_records_2(self.entry_search_2.get()))
        btn_search_2.bind('<Button-1>', lambda event: self.destroy(), add='+')

        lbl_search_5 = tk.Label(self, text='Поиск в видача книг')
        lbl_search_5.place(x=10, y=140)

        self.entry_search_5 = ttk.Entry(self)
        self.entry_search_5.place(x=135, y=140, width=150)

        btn_cansel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cansel.place(x=185, y=170)

        btn_search_5 = ttk.Button(self, text='Поиск')
        btn_search_5.place(x=105, y=170)
        btn_search_5.bind('<Button-1>', lambda event: self.view.search_records_5(self.entry_search_5.get()))
        btn_search_5.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.c = self.conn.cursor()

    def insert_data(self, nazva, avtor, janor, cina):
        self.c.execute('''INSERT INTO книги(название, автор, жанр, стоимость) VALUES (?,?,?,?)''',
                       (nazva, avtor, janor, cina))
        self.conn.commit()

    def insert_data_2(self, fio, tell):
        self.c.execute('''INSERT INTO читатели(ФИО, телефон) VALUES (?,?)''', (fio, tell))
        self.conn.commit()

    def insert_data_5(self, book, reader, given):
        self.c.execute('''INSERT INTO видача_Книг(кодКниги, кодЧитателя, датаВыдачи) VALUES (?,?,?)''', (book, reader, given))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Бібліотека")
    root.geometry("700x500+350+100")
    # root.resizable(False, False)
    root.mainloop()
