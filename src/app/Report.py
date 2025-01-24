from ClientRepository import ClientRepository
from BookRepository import BookRepository
from BookLoanRepository import BookLoanRepository
from datetime import datetime as date
from tkinter import messagebox


class Report:
    def generate_report(self):
        try:
            _dir_report = f"reports/report-{date.now().second}-{date.now().minute}-{date.now().hour}-{date.now().day}-{date.now().month}-{date.now().year}.txt"

            with open(_dir_report, "x") as file:
                for clients in ClientRepository().findAll():
                    _text_clients = f"Nome: {clients[0]}\nEmail: {clients[1]}\nNumero de Telefone: {clients[2]}\nData de Aniversario: {clients[3]}\n\n"
                    file.write("Cliente:\n\n")
                    file.write(_text_clients)
                
                file.write("--------------------------------------------------\n\n")

                for book in BookRepository().findAll():
                    _text_books = f"Titulo: {book[0]}\nAutor: {book[1]}\nGenero: {book[2]}\nClassificação Indicativa: {book[3]}\nNumero de Paginas: {book[4]}\n\n"
                    file.write("Livro:\n\n")
                    file.write(_text_books)

                file.write("--------------------------------------------------\n\n")

                for data in BookLoanRepository().find_all():

                    book_ = BookRepository().findById(data[0])[0]
                    client_ = ClientRepository().findById(data[1])[0]

                    if data[3] is None:
                        return_date = "Indefinido"

                    _text_loans_books = f"Titulo do Livro: {book_[0]}\nNome do Cliente: {client_[0]}\nData de Emprestimo: {data[2]}\nData de Retorno: {return_date}\n\n"
                    file.write("Emprestimo:\n\n")
                    file.write(_text_loans_books)

                file.write("--------------------------------------------------\n\n")
            messagebox.showinfo("Sucesso", f"arquivo de relatorio de titulo ({_dir_report}) foi criado com sucesso!")
        except FileExistsError as e:
            messagebox.showerror("Erro!", "Erro ao tentar manipular arquivos!")
            
    