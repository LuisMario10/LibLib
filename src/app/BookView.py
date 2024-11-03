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
        self.file_menu.add_command(label="Relatório", command=self.goto_report)
        self.file_menu.add_separator() 
        self.file_menu.add_command(label="Sair", command=self.window.quit)
        
        
        self.window.config(menu=self.file_menu)

        self.frame_up = self.frame_model(width_=310, height_=50, bg_color=self.color_3, row_=0, column_=0)

        self.frame_mid = self.frame_model(width_=310, height_=400, bg_color=self.darkgreen, row_=1, column_=0)

        self.frame_right = self.frame_model(width_=640, height_=403, bg_color=self.color_5, row_=0, column_=1)
        self.frame_right.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)


        self.app_name = Label(self.frame_up, text='Gerenciar Livros', anchor=NW, font=('arial 15 bold'), bg=self.color_3, fg=self.darkgreen, relief='flat')
        self.app_name.place(x=10, y=20)

        self.label_model("Titulo: ", 10, 10)
        self.entry_title = self.entry_model(45, 10, 40)

        self.label_model("Autor: ", 10, 80)
        self.entry_author = self.entry_model(45, 10, 110)

        self.label_model("Gênero: ", 10, 150)
        self.combobox_list = ["Aventura", "Ação", "Drama", "Romance", "Comedia Romantica", "Adulto", "Tecnico", "Ficção Científica", "Religioso", "Receitas", "Folclore Brasileiro"]
        self.entry_gender = ttk.Combobox(self.frame_mid, values=self.combobox_list, width=20)
        self.entry_gender.place(x=10, y=180)

        self.label_model("Classificação Indicativa: ", x_place=10, y_place=220)
        self.entry_indicate_rating= self.entry_model(width_=45, x_place=10, y_place=250)

        self.label_model("Numero de Paginas: ", x_place=10, y_place=290)
        self.entry_number_of_pages = self.entry_model(width_=45, x_place=10, y_place=320)


        self.button_model(text_="Cadastrar", bg_color=self.color_3, fg_color=self.darkgreen, function=self.post, x_place=215, y_place=370)

        self.button_model(text_="Atualizar", bg_color='blue', fg_color='lightblue', function=self.update, x_place=115, y_place=370)

        self.button_model(text_="Deletar", bg_color='darkred', fg_color="#ff6961", function=None, x_place=15, y_place=370)
        
        self.get_all(self.frame_right)

        self.window.mainloop()

    def frame_model(self, width_, height_, bg_color, row_, column_):
        frame = Frame(self.window, width=width_, height=height_, bg=bg_color, relief='flat')
        frame.grid(row=row_, column=column_)
        return frame


    def label_model(self, text_, x_place, y_place):
        label = Label(self.frame_mid, text=text_, anchor=NW, font=('arial 12 bold'), bg=self.darkgreen, fg=self.white, relief='flat')
        label.place(x=x_place, y=y_place)
        return label


    def entry_model(self, width_, x_place, y_place):
        entry = Entry(self.frame_mid, width=width_, justify='left', relief='solid')
        entry.place(x=x_place, y=y_place)
        return entry


    def button_model(self, text_, bg_color, fg_color, function, x_place, y_place):
        button = Button(self.frame_mid, text=text_, width=8, anchor=NW, font=('arial 10 bold'), bg=bg_color, fg=fg_color, relief='raised', overrelief='ridge', command=function)
        button.place(x=x_place, y=y_place)
        return button

    def goto_book_loan_area(self):
        pass

    def goto_client_area(self):
        __init__.ClientView()


    def goto_report(self):
        pass


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
        window_update = Toplevel()
        window_update.geometry("800x600")
        window_update.configure(background=self.color_2)
        window_update.resizable(width=FALSE, height=FALSE)

        frame_ =  Frame(window_update, width=800, height=75, bg=self.darkgreen, relief='flat')
        frame_.grid(row=0, column=0)

        name_top  = Label(self.frame_, text='Atualizar Livros', anchor=NW, font=('arial 15 bold'), bg=self.color_3, fg=self.darkgreen, relief='flat')
        self.app_name.place(x=10, y=20)

        label_title = Label(window_update, text="Titulo Atual", anchor=NW, font=('arial 12 bold'), bg=self.color_2, fg=self.darkgreen, relief='flat')
        label_title.place(x=40, y=100)

        entry_before_title = Entry(window_update, width=45, justify='left', relief='solid')
        entry_before_title.place(x=40, y=130)

        label_update_title = Label(window_update, text="Titulo Novo", anchor=NW, font=('arial 12 bold'), bg=self.color_2, fg=self.darkgreen, relief='flat')
        label_update_title.place(x=40, y=170)

        entry_update_title = Entry(window_update, width=45, justify='left', relief='solid')
        entry_update_title.place(x=40, y=200)

        label_update_author = Label(window_update, text="Novo Autor", anchor=NW, font=('arial 12 bold'), bg=self.color_2, fg=self.darkgreen, relief='flat')
        label_update_author.place(x=40, y=240)

        entry_update_author = Entry(window_update, width=45, justify='left', relief='solid')
        entry_update_author.place(x=40, y=270)

        label_update_gender = Label(window_update, text="Novo Genero", anchor=NW, font=('arial 12 bold'), bg=self.color_2, fg=self.darkgreen, relief='flat')
        label_update_gender.place(x=40, y=310)
        entry_update_gender = ttk.Combobox(window_update, values=self.combobox_list, width=20)
        entry_update_gender.place(x=40, y=340)

        label_update_indicate_rating = Label(window_update, text="Classificação Indicativa:", anchor=NW, font=('arial 12 bold'), bg=self.color_2, fg=self.darkgreen, relief='flat')
        label_update_indicate_rating.place(x=40, y=410)

        entry_update_indicate_rating = Entry(window_update, width=45, justify='left', relief='solid')
        entry_update_indicate_rating.place(x=40, y=440)

        label_update_number_of_pages = Label(window_update, text="Numero de Paginas:", anchor=NW, font=('arial 12 bold'), bg=self.color_2, fg=self.darkgreen, relief='flat')
        label_update_number_of_pages.place(x=40, y=480)

        entry_update_number_of_pages = Entry(window_update, width=45, justify='left', relief='solid')
        entry_update_number_of_pages.place(x=40, y=510)

        title_now = entry_before_title.get()

        new_title = entry_update_title.get()
        new_author = entry_update_author.get()
        new_gender = entry_update_gender.get()
        new_indicate_rating = entry_update_indicate_rating.get()
        new_number_of_pages = entry_update_number_of_pages.get()

        list_data_update = [new_title, new_author, new_gender, new_indicate_rating, new_number_of_pages, new_title]

        def request():
            BookRepository().update(list_data_update)

            for widget in self.frame_right.winfo_children():
                widget.destroy()

            self.get_all(self.frame_right)

            messagebox.showinfo("Sucesso!", "Livro atualizado com sucesso!")

        button_confirm_update = Button(window_update, text="Confirmar", width=8, anchor=NW, font=('arial 10 bold'), bg=self.darkgreen, fg=self.color_4, relief='raised', overrelief='ridge', command=request)
        button_confirm_update.place(x=215, y=520)
