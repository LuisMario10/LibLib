import sqlite3

# username: admin@liblib.auth
# senha: fpAss10$a

class AuthService:
    def __init__(self):
        self.database = sqlite3.connect('src/database/liblib.db')
        self.cursor = self.database.cursor()


    def login(self, username, password):
        query = "SELECT * FROM Admin"
        with self.database:
            self.cursor.execute(query)

        result = self.cursor.fetchall()

        for data in result:
            if data[0] == username and data[1] == password:
                return True
        return False



    def sign_in(self, username, password):
        query = "INSERT INTO Authentication(username, password) VALUES (?, ?)"
        data = [username, password]
        with self.database:
            self.cursor.execute(query, data)

