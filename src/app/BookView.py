from tkinter import *
from tkinter import ttk
from BookRepository import BookRepository
from uuid import uuid4
from tkinter import messagebox
import __init__

class BookView:
    global BookView

    def __init__(self):
        #Define color
        self.darkgreen = "#006400" #dark green
        self.color_2 = "#57f507"
        self.color_3 = "#3df588"
        self.color_4 = "#07f517"
        self.color_5 = "#6cf575"
        self.white = "#ffffff"
        self.black = "#000000"

        self.window = Tk()
        self.window.title("LibLib - Gerenciador de Bibliotecas")
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.geometry("1028x514")
        self.window.configure(background=self.darkgreen)

        self.main_menu = Menu(self.window)

        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label="Area Emprestimos", command=self.goto_book_loan_area)
        self.file_menu.add_command(label="Area Cliente", command=self.goto_client_area)
        self.file_menu.add_command(label="Relatório", command=__init__.Report().generate_report)
        self.file_menu.add_separator() 
        self.file_menu.add_command(label="Sair", command=self.window.quit)
        
        
        self.window.config(menu=self.file_menu)

        self.frame_up = self.frame_model(self.window, width_=310, height_=50, bg_color=self.color_3, row_=0, column_=0)

        self.frame_mid = self.frame_model(self.window, width_=310, height_=400, bg_color=self.darkgreen, row_=1, column_=0)

        self.frame_right = self.frame_model(self.window, width_=640, height_=403, bg_color=self.color_5, row_=0, column_=1)
        self.frame_right.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)


        self.app_name = Label(self.frame_up, text='Gerenciar Livros', anchor=NW, font=('arial 15 bold'), bg=self.color_3, fg=self.darkgreen, relief='flat')
        self.app_name.place(x=10, y=20)

        self.label_model(self.frame_mid, "Titulo: ", 10, 10)
        self.entry_title = self.entry_model(self.frame_mid, 45, 10, 40)

        self.label_model(self.frame_mid, "Autor: ", 10, 80)
        self.entry_author = self.entry_model(self.frame_mid, 45, 10, 110)

        self.label_model(self.frame_mid, "Gênero: ", 10, 150)
        self.combobox_list = ["Aventura", "Ação", "Drama", "Romance", "Comedia Romantica", "Adulto", "Tecnico", "Ficção Científica", "Religioso", "Receitas", "Folclore Brasileiro"]
        self.entry_gender = ttk.Combobox(self.frame_mid, values=self.combobox_list, width=20)
        self.entry_gender.place(x=10, y=180)

        self.label_model(self.frame_mid, "Classificação Indicativa: ", x_place=10, y_place=220)
        self.entry_indicate_rating= self.entry_model(widget=self.frame_mid, width_=45, x_place=10, y_place=250)

        self.label_model(self.frame_mid, "Numero de Paginas: ", x_place=10, y_place=290)
        self.entry_number_of_pages = self.entry_model(widget=self.frame_mid, width_=45, x_place=10, y_place=320)


        self.button_model(widget=self.frame_mid,text_="Cadastrar", bg_color=self.color_3, fg_color=self.darkgreen, function=self.post, x_place=215, y_place=370)

        self.button_model(widget=self.frame_mid, text_="Atualizar", bg_color='blue', fg_color='lightblue', function=self.update, x_place=115, y_place=370)

        self.button_model(widget=self.frame_mid ,text_="Deletar", bg_color='darkred', fg_color="#ff6961", function=self.delete, x_place=15, y_place=370)
        
        self.get_all(self.frame_right)

        self.window.mainloop()

    def frame_model(self, window, width_, height_, bg_color, row_, column_):
        frame = Frame(window, width=width_, height=height_, bg=bg_color, relief='flat')
        frame.grid(row=row_, column=column_)
        return frame


    def label_model(self, widget ,text_, x_place, y_place):
        label = Label(widget, text=text_, anchor=NW, font=('arial 12 bold'), bg=self.darkgreen, fg=self.white, relief='flat')
        label.place(x=x_place, y=y_place)
        return label


    def entry_model(self, widget, width_, x_place, y_place):
        entry = Entry(widget, width=width_, justify='left', relief='solid')
        entry.place(x=x_place, y=y_place)
        return entry


    def button_model(self, widget, text_, bg_color, fg_color, function, x_place, y_place):
        button = Button(widget, text=text_, width=8, anchor=NW, font=('arial 10 bold'), bg=bg_color, fg=fg_color, relief='raised', overrelief='ridge', command=function)
        button.place(x=x_place, y=y_place)
        return button

    def goto_book_loan_area(self):
        __init__.BookLoanView()

    def goto_client_area(self):
        __init__.ClientView()


    def get_all(self, frame):
        #Scrollbar
        global tree

        self.header = ["Titulo", "Autor", "Genero", "Class. Indicativa" ,"Num. de Paginas"]

        tree = ttk.Treeview(frame, selectmode="extended", columns=self.header,
        show="headings")

        vertical_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)

        horizontal_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

        tree.grid(column=0, row=0, sticky='nsew')
        vertical_scrollbar.grid(column=1, row=0, sticky='ns')
        horizontal_scrollbar.grid(column=0, row=1, sticky='ew')
        frame.grid_rowconfigure(0, weight=12)

        position_anchor = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
        column_width=[140, 120, 110, 100, 120, 60, 40]
        loop_count=0

        for col in self.header:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=column_width[loop_count], anchor=position_anchor[loop_count])
            loop_count+=1

        for item in BookRepository().findAll():
            tree.insert('', 'end', values=item)

    
    def post(self):
        title = self.entry_title.get()
        author = self.entry_author.get()
        gender = self.entry_gender.get()
        indicate_rating = self.entry_indicate_rating.get()
        number_of_pages = self.entry_number_of_pages.get()

        list_input = [str(uuid4()), title, author, gender, indicate_rating, number_of_pages]

        if len(title) == 0:
            messagebox.showerror("Erro!", "O campo titulo não pode ser vazio!")
        elif len(author) == 0:
            messagebox.showerror("Erro!", "O campo author não pode ser vazio!")
        elif len(gender) == 0:
            messagebox.showerror("Erro!", "O campo gênero não pode ser vazio!")
        elif len(indicate_rating) == 0:
            messagebox.showerror("Erro!", "O campo classificação indicativa não pode ser vazio!")
        if len(number_of_pages) == 0:
            messagebox.showerror("Erro!", "O campo numero de páginas pode ser vazio!")
        else:
            BookRepository().create(list_input)
            messagebox.showinfo("Sucesso!", "Dados cadastrados com sucesso!")

            self.entry_title.delete(0, 'end')
            self.entry_author.delete(0, 'end')
            self.entry_gender.delete(0, 'end')
            self.entry_indicate_rating.delete(0, 'end')
            self.entry_number_of_pages.delete(0, 'end')
        
        for widget in self.frame_right.winfo_children():
            widget.destroy()
        
        self.get_all(self.frame_right)
 
    def update(self):
        window_update = Tk()
        window_update.title("LibLib - Gerenciador de Bibliotecas")
        window_update.resizable(width=FALSE, height=FALSE)
        window_update.geometry("800x500")
        window_update.configure(background=self.darkgreen)

        self.label_model(window_update, "Titulo Atual: ", 10, 10)
        self.entry_before_title = self.entry_model(window_update, 45, 10, 40)

        self.label_model(window_update, "Titulo Novo:", 10, 80)
        self.entry_new_title = self.entry_model(window_update, 45, 10, 110)

        self.label_model(window_update, "Autor: ", 10, 150)
        self.entry_new_author = self.entry_model(window_update, 45, 10, 180)

        self.label_model(window_update, "Gênero: ", 10, 220)
        self.entry_new_gender = ttk.Combobox(window_update, values=self.combobox_list, width=20)
        self.entry_new_gender.place(x=10, y=250)


        self.label_model(window_update,"Classificação Indicativa: ", x_place=10, y_place=290)
        self.entry_new_indicate_rating= self.entry_model(widget=window_update ,width_=45, x_place=10, y_place=320)

        self.label_model(window_update, "Numero de Paginas: ", x_place=10, y_place=360)
        self.entry_new_number_of_pages = self.entry_model(widget=window_update, width_=45, x_place=10, y_place=390)

        self.button_model(widget=window_update, text_="Confirmar", bg_color=self.color_3, fg_color=self.darkgreen, function=self.request_update, x_place=10, y_place=460)

        self.button_model(widget=window_update, text_="Sair", bg_color='red', fg_color='white', function=quit, x_place=100, y_place=460)
    
    def request_update(self):        
        list_update = [self.entry_new_title.get(), self.entry_new_author.get(), self.entry_new_gender.get(), self.entry_new_indicate_rating.get(), self.entry_new_number_of_pages.get(), self.entry_before_title.get()]

        BookRepository().update(list_update)
        messagebox.showinfo("Sucesso!", "Dados atualizados com sucesso")
        datas = BookRepository().findAll()

        for item in datas:
            print(f"{item}")
        
        for widget in self.frame_right.winfo_children():
            widget.destroy()
        
        self.get_all(self.frame_right)
    
    def delete(self):
        treev_data = tree.focus()
        treev_converter = tree.item(treev_data)
        tree_list = treev_converter['values']

        self.entry_title.delete(0, 'end')
        self.entry_author.delete(0, 'end')
        self.entry_gender.delete(0, 'end')
        self.entry_indicate_rating.delete(0, 'end')
        self.entry_number_of_pages.delete(0, 'end')

        self.entry_title.insert(0, tree_list[0])
        self.entry_author.insert(0, tree_list[1])
        self.entry_gender.insert(0, tree_list[2])
        self.entry_indicate_rating.insert(0, tree_list[3])
        self.entry_number_of_pages.insert(0, tree_list[4])

        self.window_delete = Tk()
        self.window_delete.resizable(width=FALSE, height=FALSE)
        self.window_delete.geometry("364x200")
        self.window_delete.configure(background=self.darkgreen)

        self.label_model(self.window_delete, "Deseja deletar esses livro?", 90, 60)
        self.button_model(self.window_delete, "Confirmar", "darkred", "white", self.delete_data, 180, 115)

    
    def delete_data(self):
        title_to_delete = self.entry_title.get()
        print(f"{title_to_delete}")
        BookRepository().delete([title_to_delete])

        for widget in self.frame_right.winfo_children():
            widget.destroy()
        
        self.get_all(self.frame_right)
