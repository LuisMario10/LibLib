from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from ClientRepository import ClientRepository
from uuid import uuid4
from tkinter import messagebox
import __init__

class ClientView:

    global ClientView

    def __init__(self):
        #Define color
        self.color_1 = "#006400" #dark green
        self.color_2 = "#57f507"
        self.color_3 = "#3df588"
        self.color_4 = "#07f517"
        self.color_5 = "#6cf575"
        self.color_6 = "#ffffff" #white
        self.color_7 = "#000000" #black

        self.window = Tk()
        self.window.title("LibLib - Gerenciador de Bibliotecas")
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.geometry("1028x514")
        self.window.configure(background=self.color_1)

        self.main_menu = Menu(self.window)

        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label="Area Emprestimos", command=self.goto_book_loan_area)
        self.file_menu.add_command(label="Area Livros", command=self.goto_book_area)
        self.file_menu.add_command(label="Relatório", command=__init__.Report().generate_report)
        self.file_menu.add_separator() 
        self.file_menu.add_command(label="Sair", command=self.window.quit)
        
        self.main_menu.add_cascade(label="Arquivo", menu=self.file_menu)
        
        self.window.config(menu=self.file_menu)

        self.frame_up = self.frame_model(width_=310, height_=50, bg_color=self.color_3, row_=0, column_=0)

        self.frame_mid = self.frame_model(310, 400, self.color_1, 1, 0)

        self.frame_right = self.frame_model(640, 403, self.color_5, 0, 1)
        self.frame_right.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

        self.app_name = Label(self.frame_up, text='Gerenciar Clientes', anchor=NW, font=('arial 15 bold'),bg=self.color_3, fg='darkgreen', relief='flat')
        self.app_name.place(x=10, y=20)

        self.label_model(self.frame_mid, "Nome: ", 10, 10)
        self.entry_name = self.entry_model(self.frame_mid, 45, 10, 40)

        self.label_model(self.frame_mid, "Email: ", 10, 80)
        self.entry_email = self.entry_model(self.frame_mid, 45, 10, 110)

        self.label_model(self.frame_mid, "Numero de Telefone: ", 10, 150)
        self.entry_phone_number = self.entry_model(self.frame_mid, 45, 10, 180)

        label_input_date_of_birth = Label(self.frame_mid, bg=self.color_1, text="Data de Nascimento: ", anchor=NW, font=('arial 12 bold'), fg=self.color_6, relief='flat')
        label_input_date_of_birth.place(x=10, y=220)

        self.entry_date_of_birth = DateEntry(self.frame_mid, width=30, foreground='white', borderwidth=2)
        self.entry_date_of_birth.place(x=10, y=250)

        self.button_model(self.frame_mid, "Cadastrar", self.color_3, 'darkgreen', function=self.post, x_place=15, y_place=350)
        self.button_model(self.frame_mid, "Atualizar", 'blue', 'lightblue', self.update, 115, 350)
        self.button_model(self.frame_mid, "Deletar", 'darkred', "#ff6961", None, 215, 350)
        
        self.get_all(self.frame_right)

        self.window.mainloop()


    def frame_model(self, width_, height_, bg_color, row_, column_):
        frame = Frame(self.window, width=width_, height=height_, bg=bg_color, relief='flat')
        frame.grid(row=row_, column=column_)
        return frame


    def label_model(self, widget, text_, x_place, y_place):
        label = Label(widget, text=text_, anchor=NW, font=('arial 12 bold'), bg=self.color_1, fg=self.color_6, relief='flat')
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
        pass

    def goto_book_area(self):
        __init__.BookView()
        


    def get_all(self, frame):
        #Scrollbar
        global tree

        self.header = ["Nome", "Email", "Numero de Telefone", "Livro Emprestado" ,"Idade"]

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
        column_width=[170, 140, 140, 100, 120, 50, 100]
        loop_count=0

        for col in self.header:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=column_width[loop_count], anchor=position_anchor[loop_count])
            loop_count+=1

        for item in ClientRepository().findAll():
            tree.insert('', 'end', values=item)

    
    def post(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone_number = self.entry_phone_number.get()
        date_of_birth = self.entry_date_of_birth.get_date()

        list_input = [str(uuid4()), name, email.lower(), "Sem emprestimos", date_of_birth, phone_number]

        if len(name) == 0:
            messagebox.showerror("Erro!", "O campo nome não pode esta vazio!")
        else:
            ClientRepository().create(list_input)
            messagebox.showinfo("Sucesso!", "Dados cadastrados com sucesso!")

            self.entry_name.delete(0, 'end')
            self.entry_email.delete(0, 'end')
            self.entry_phone_number.delete(0, 'end')
        
        for widget in self.frame_right.winfo_children():
            widget.destroy()
        
        self.get_all(self.frame_right)
    
    def update(self):
        window_update = Tk()
        window_update.title("LibLib - Gerenciador de Bibliotecas")
        window_update.resizable(width=FALSE, height=FALSE)
        window_update.geometry("400x400") 
        window_update.configure(background=self.color_1)

        self.label_model(window_update, "Email Atual: ", 10, 10)
        self.entry_before_email = self.entry_model(window_update, 45, 10, 40)

        self.label_model(window_update, "Email Novo:", 10, 80)
        self.entry_new_email = self.entry_model(window_update, 45, 10, 110)

        self.label_model(window_update, "Nome: ", 10, 150)
        self.entry_new_name = self.entry_model(window_update, 45, 10, 180)

        self.label_model(window_update, "Numero de Telefone: ", 10, 220)
        self.entry_new_phone_number = self.entry_model(window_update, 45, 10, 250)

        self.label_model(window_update, "Data Nascimento: ", x_place=10, y_place=290)
        self.entry_new_date_of_birth = DateEntry(window_update, width=30, foreground='white', borderwidth=2)
        self.entry_new_date_of_birth.place(x=10, y=320)

        self.button_model(widget=window_update, text_="Confirmar", bg_color=self.color_3, fg_color=self.color_1, function=self.request_update, x_place=10, y_place=370)

        self.button_model(widget=window_update, text_="Sair", bg_color='red', fg_color='white', function=quit, x_place=100, y_place=370)
    
    def request_update(self):        
        list_update = [self.entry_new_name.get(), self.entry_new_email.get(), self.entry_new_date_of_birth.get_date(), self.entry_new_phone_number.get(), self.entry_before_email.get()]

        ClientRepository().update(list_update)
        messagebox.showinfo("Sucesso!", "Dados Atualizados com sucesso")
        
        for widget in self.frame_right.winfo_children():
            widget.destroy()
        
        self.get_all(self.frame_right)
    
    # def delete(self):
    #     treev_data = tree.focus()
    #     treev_converter = tree.item(treev_data)
    #     tree_list = treev_converter['values']

    #     self.entry_title.delete(0, 'end')
    #     self.entry_author.delete(0, 'end')
    #     self.entry_gender.delete(0, 'end')
    #     self.entry_indicate_rating.delete(0, 'end')
    #     self.entry_number_of_pages.delete(0, 'end')

    #     self.entry_title.insert(0, tree_list[0])
    #     self.entry_author.insert(0, tree_list[1])
    #     self.entry_gender.insert(0, tree_list[2])
    #     self.entry_indicate_rating.insert(0, tree_list[3])
    #     self.entry_number_of_pages.insert(0, tree_list[4])

    #     self.window_delete = Tk()
    #     self.window_delete.resizable(width=FALSE, height=FALSE)
    #     self.window_delete.geometry("364x200")
    #     self.window_delete.configure(background=self.darkgreen)

    #     self.label_model(self.window_delete, "Deseja deletar esses livro?", 90, 60)
    #     self.button_model(self.window_delete, "Confirmar", "darkred", "white", self.delete_data, 180, 115)

    
    # def delete_data(self):
    #     title_to_delete = self.entry_title.get()
    #     print(f"{title_to_delete}")
    #     BookRepository().delete([title_to_delete])

    #     for widget in self.frame_right.winfo_children():
    #         widget.destroy()
        
    #     self.get_all(self.frame_right)


