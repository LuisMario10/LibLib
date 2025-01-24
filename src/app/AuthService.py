import sqlite3

class AuthService:
    def __init__(self):
        self.database = sqlite3.connect('src/database/liblib.db')
        self.cursor = self.database.cursor()


    def login(self, username, password):
        try:
            query = "SELECT * FROM Admin"
            with self.database:
                self.cursor.execute(query)

            for data in self.cursor.fetchall():
                if data[0] == username and data[1] == password:
                    return True
            return False
        except Exception as e:
            print(f"Error - See exception: {e}")
            

    def sign_in(self, username, password):
        try:
            query = "INSERT INTO Admin(username, password) VALUES (?, ?)"

            if username is None :
                return Exception
            
            if password is None:
                return Exception
            
            data = [username, password]
            with self.database:
                self.cursor.execute(query, data)
                
        except Exception as e:
            print(f"Error to signin - See exception: {e}")
