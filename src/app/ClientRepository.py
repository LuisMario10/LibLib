import sqlite3

class ClientRepository:

    def __init__(self):
        self.database = sqlite3.connect("src/database/liblib.db")
        self.cursor = self.database.cursor()
        
    def create(self, datas):
        query = "INSERT INTO Client (id, name, email, loan_book, date_of_birth, phone_number) VALUES (?,?,?,?,?,?)"
        with self.database:
            self.cursor.execute(query, datas)
    
    def findAll(self):
        list_result = []
        query = "SELECT name, email, phone_number, loan_book, date_of_birth FROM Client"
        with self.database:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for data in result:
                list_result.append(data)
        return list_result
    
    def findById(self, id):
        query = "SELECT * FROM Client WHERE id = ?"
        with self.database:
            self.cursor.execute(query, id)
            return self.cursor.fetchall()
    
    def findByEmail(self, email):
        query = "SELECT * FROM Client WHERE email = ?"
        with self.database:
            self.cursor.execute(query, email)
            return self.cursor.fetchall()
    
    def update(self, new_datas):
        query = "UPDATE Client SET name=?, email=?, date_of_birth=?, phone_number=? WHERE id = ?"
        with self.database:
            self.cursor.execute(query, new_datas)
            
            print("Dados do cliente foram atualizados")

    def delete(self, id):
        query = "DELETE FROM Client WHERE id = ?"
        with self.database:
            self.cursor.execute(query, id)

            print(f"O Cliente de id {id} foi Deletado do Banco de Dados com sucesso")


