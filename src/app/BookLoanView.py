from tkinter import *
from tkinter import ttk
from BookRepository import BookRepository
from uuid import uuid4
from tkinter import messagebox
import __init__

class BookLoanView:
    global BookLoanView

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
        self.file_menu.add_command(label="Area Livros", command=self.goto_book_area)
        self.file_menu.add_command(label="Area Cliente", command=self.goto_client_area)
        self.file_menu.add_command(label="Gerar Relatório", command=self.goto_report)
        self.file_menu.add_separator() 
        self.file_menu.add_command(label="Sair", command=self.window.quit)
        
        
        self.window.config(menu=self.file_menu)

        self.frame_up = self.frame_model(self.window, width_=310, height_=50, bg_color=self.color_3, row_=0, column_=0)

        self.frame_mid = self.frame_model(self.window, width_=310, height_=400, bg_color=self.darkgreen, row_=1, column_=0)

        self.frame_right = self.frame_model(self.window, width_=640, height_=403, bg_color=self.color_5, row_=0, column_=1)
        self.frame_right.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)


        self.app_name = Label(self.frame_up, text='Gerenciar Emprestimos', anchor=NW, font=('arial 15 bold'), bg=self.color_3, fg=self.darkgreen, relief='flat')
        self.app_name.place(x=10, y=20)

        self.label_model(self.frame_mid, "Email do Cliente: ", 10, 10)
        self.entry_client_email = self.entry_model(self.frame_mid, 45, 10, 40)

        self.label_model(self.frame_mid, "Nome do Livro: ", 10, 80)
        self.entry_book_title = self.entry_model(self.frame_mid, 45, 10, 110)

        self.label_model(self.frame_mid, "Tempo de Emprestimo: ", 10, 140)
        self.entry_date_of_birth = DateEntry(self.frame_mid, width=30, foreground='white', borderwidth=2)
        self.entry_date_of_birth.place(x=10, y=180)


        self.button_model(widget=self.frame_mid,text_="Cadastrar", bg_color=self.color_3, fg_color=self.darkgreen, function=self.post, x_place=215, y_place=210)

        self.button_model(widget=self.frame_mid, text_="Atualizar", bg_color='blue', fg_color='lightblue', function=self.update, x_place=115, y_place=210)

        self.button_model(widget=self.frame_mid ,text_="Deletar", bg_color='darkred', fg_color="#ff6961", function=self.delete, x_place=15, y_place=210)
        
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

    def goto_book_area(self):
        __init__.BookView()

    def goto_client_area(self):
        __init__.ClientView()


    def goto_report(self):
        __init__.Report()

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
        client_email = self.entry_client_email.get().lower()
        book_title = self.entry_book_title.get()
        time_to_loan = self.entry_time_to_loan.get()
        

        list_input = [str(uuid4()), client_email, book_title, time_to_loan,]

        if len(name) == 0:
            messagebox.showerror("Erro!", "O campo nome não pode esta vazio!")
        else:
            ().create(list_input)
            messagebox.showinfo("Sucesso!", "Dados cadastrados com sucesso!")

            self.entry_name.delete(0, 'end')
            self.entry_email.delete(0, 'end')
            self.entry_phone_number.delete(0, 'end')
        
        for widget in self.frame_right.winfo_children():
            widget.destroy()
        
        self.get_all(self.frame_right)