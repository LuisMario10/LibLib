from tkinter import *
from tkinter import messagebox
from AuthService import AuthService
from __init__ import *

class AuthView:

    def __init__(self):

        self.darkgreen = "#006400" 
        self.color_2 = "#57f507"
        self.color_3 = "#3df588"
        self.color_4 = "#07f517"
        self.color_5 = "#6cf575"
        self.white = "#ffffff"
        self.black = "#000000" 
    
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.title("Login - LibLib")
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.configure(background=self.darkgreen)

        self.frame_top = self.frame_model(width_=800, height_=60, bg_color=self.color_3, row_=0, column_=0)

        self.frame_mid = self.frame_model(width_=800, height_=400, bg_color=self.color_4, row_=1, column_=0)

        self.frame_down = self.frame_model(width_=800, height_=140, bg_color=self.darkgreen, row_=2, column_=0)


        self.app_name = Label(self.frame_top, text='Login - LibLib APP', anchor=NW, font=('arial 20 bold'), bg=self.color_3, fg='darkgreen', relief='flat')
        self.app_name.place(x=300, y=18)

        self.label_username = self.label_model(frame=self.frame_mid, text_="Nome do Usuario:", x_place=276, y_place=84)
        self.entry_username = self.entry_model(52, 276, 116)

        self.label_password = self.label_model(frame=self.frame_mid, text_="Senha:", x_place=276, y_place=176)
        self.entry_password = self.entry_model(52, 276, 206)

        self.button_confirm = self.button_model(text_="Confirmar", bg_color=self.darkgreen, fg_color='lightgreen', function=self.try_login, x_place=504, y_place=256)

        self.button_clean_inputs = self.button_model(text_="Apagar", bg_color="gray", fg_color='lightgray', function=self.clean_inputs, x_place=390, y_place=256)

        self.button_quit = self.button_model(text_="Sair", bg_color='darkred', fg_color='#ff6961', function=self.window.quit, x_place=276, y_place=256)

        self.description_footer = Label(self.frame_down, text="Gerencie sua biblioteca com LibLib - Temos Funcionalidades que vão agilizar seu negócio!", anchor=CENTER, font=('arial 12 bold'), bg=self.darkgreen, fg=self.white, relief='flat')
        self.description_footer.pack()
        
    def frame_model(self, width_, height_, bg_color, row_, column_):
        frame = Frame(self.window, width=width_, height=height_, bg=bg_color, relief='flat')
        frame.grid(row=row_, column=column_)
        return frame


    def label_model(self, frame,text_, x_place, y_place):
        label = Label(frame, text=text_, anchor=NW, font=('arial 16 bold'), bg=self.color_4, fg=self.darkgreen, relief='flat')
        label.place(x=x_place, y=y_place)
        return label


    def entry_model(self, width_, x_place, y_place):
        entry = Entry(self.frame_mid, width=width_, justify='left', relief='solid')
        entry.place(x=x_place, y=y_place)
        return entry


    def button_model(self, text_, bg_color, fg_color, function, x_place, y_place):
        button = Button(self.frame_mid, text=text_, width=8, anchor=NW, font=('arial 12 bold'), bg=bg_color, fg=fg_color, relief='raised', overrelief='ridge', command=function)
        button.place(x=x_place, y=y_place)
        return button


    def try_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()


        if len(username) == 0 or len(password) == 0:
            messagebox.showerror("Erro nos campos!", "Campo nome do usuario e o campo senha não podem estar vazios!")

            
        if not AuthService().login(username, password):
            messagebox.showinfo("Acesso negado!", "Login falhou! Tente novamente")
            self.entry_username.delete(0, 'end')
            self.entry_password.delete(0, 'end')
        else:
            messagebox.showinfo("Acesso permitido!", "Login executado com sucesso!. Aproveite o App")
            self.window.destroy()
            BookView()
        

    def clean_inputs(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if len(username) == 0 and len(password) == 0:
            messagebox.showwarning("Atenção!", "Campos já estão vazios")
        else:
            self.entry_username.delete(0, 'end')
            self.entry_password.delete(0, 'end')
    
_MAIN = AuthView()
_MAIN.window.mainloop()
