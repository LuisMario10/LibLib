import sqlite3

class BookRepository:
    def __init__(self):
        self.database = sqlite3.connect("src/database/liblib.db")
        self.cursor = self.database.cursor()
        
    def create(self, datas):
        try:
            query = "INSERT INTO Book (id, title, author, gender, indicate_rating, number_of_pages) VALUES (?,?,?,?,?,?)"
            with self.database:
                self.cursor.execute(query, datas)

        except sqlite3.Error as e:
            print(f"Erro ao criar registro de livro: {e}")
    
    def findAll(self):
        try:
            list_result = []
            query = "SELECT title, author, gender, indicate_rating, number_of_pages FROM Book"
            with self.database:
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                for data in result:
                    list_result.append(data)
            return list_result

        except sqlite3.Error as e:
            print(f"Erro ao procurar todos os livros: \n{e}")
    
    def findById(self, id):
        try:
            query = "SELECT title, author, gender, indicate_rating, number_of_pages FROM Book WHERE id = ?"
            with self.database:
                self.cursor.execute(query, (id,))
                return self.cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Erro ao procurar livro por id: {e}")
                                                                                                                                                                                              
    def findByTitle(self, title):
        try:
            query = "SELECT * FROM Book WHERE title = ?"
            with self.database:
                self.cursor.execute(query, title)
                return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao procurar livro por titulo: {e}")
    
    
    def update(self, new_datas):
        try:
            query = "UPDATE Book SET title=?, author=?, gender=?, indicate_rating=?, number_of_pages=? WHERE title = ?"
            with self.database:
                self.cursor.execute(query, new_datas)
        except sqlite3.Error as e:
            print(f"Erro ao atualizar livro: {e}")


    def delete(self, title):
        try:
            query = "DELETE FROM Book WHERE title = ?"
            with self.database:
                self.cursor.execute(query, title)
        except sqlite3.Error as e:
            print(f"Erro ao deletar livro: {e}")

