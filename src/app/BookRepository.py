import sqlite3

class BookRepository:

    def __init__(self):
        self.database = sqlite3.connect("src/database/liblib.db")
        self.cursor = self.database.cursor()
        
    def create(self, datas):
        query = "INSERT INTO Book (id, title, author, gender, indicate_rating, number_of_pages) VALUES (?,?,?,?,?,?)"
        with self.database:
            self.cursor.execute(query, datas)
    
    def findAll(self):
        list_result = []
        query = "SELECT title, author, gender, indicate_rating, number_of_pages FROM Book"
        with self.database:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for data in result:
                list_result.append(data)
        return list_result
    
    def findById(self, id):
        query = "SELECT * FROM Book WHERE id = ?"
        with self.database:
            self.cursor.execute(query, id)
            return self.cursor.fetchall()
                                                                                                                                                                                                                                                                                                                    
    def findByTitle(self, title):
        query = "SELECT * FROM Book WHERE title = ?"
        with self.database:
            self.cursor.execute(query, title)
            return self.cursor.fetchall()
    
    
    def update(self, new_datas):
        try:
            query = "UPDATE Book SET title=?, author=?, gender=?, indicate_rating=?, number_of_pages=? WHERE title = ?"
            with self.database:
                self.cursor.execute(query, new_datas)
        except Exception as e:
            print(f"Deu erro {e}")


    def delete(self, title):
        try:
            query = "DELETE FROM Client WHERE title = ?"
            with self.database:
                self.cursor.execute(query, title)
        except Exception as e:
            print(f"Deu erro: {e}")


