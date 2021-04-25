import config

class database_extract():
    def get_info_from_database(self):
        self.cursor = config.conn.cursor()
        self.cursor.execute("SELECT * FROM registered_users")
        self.users = self.cursor.fetchone()
        return self.users

    def parse_information(self):
        self.get_info_from_database()    
        self.user_number = self.users[0]
        self.user_number = f"{self.user_number}@sistemas.frc.utn.edu.ar"
        self.user_password = self.users[1]
        return self.user_number, self.user_password 




