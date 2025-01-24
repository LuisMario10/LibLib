import sqlite3
import uuid

class BookLoanRepository:
    def __init__(self):
        self.database = sqlite3.connect("src/database/liblib.db")
        self.cursor = self.database.cursor()
    
    def create(self, datas):
        try:
            query  = "INSERT INTO BookLoan (id, book, client, loan_date, return_date) VALUES (?,?,?,?,?)"
            with self.database:
                self.cursor.execute(query, datas)
                print("Registro de emprestimo criado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao criar regisro de emprestimo: {e}")

    def find_all(self):
        list_result = []
        query = "SELECT book, client, loan_date, return_date FROM BookLoan"
        with self.database:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for data in result:
                list_result.append(data)
        return list_result

    
    def delete(self, data):
        try:
            query = "DELETE FROM BookLoan WHERE client=?"
            with self.database:
                self.cursor.execute(query, data)
                print("Registro excluido com sucesso")

        except sqlite3.Error as e:
            print(f"Erro ao deletar registro de emprestimo: {e}")
