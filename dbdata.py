import config

class database_extract():

    def __init__(self):
        self.cursor = config.cursor

    def get_users_to_use(self):
        self.cursor.execute("SELECT id FROM registered_users WHERE used = 0")
        self.allcredentials = self.cursor.fetchall()

        return self.allcredentials

    def get_info_from_database(self, id):
        self.cursor.execute("SELECT user, pass FROM registered_users WHERE id = ?",(id))
        self.user = self.cursor.fetchone()
        return self.user

    def parse_information(self,id):
        """Devuelve:   $user_number el usuario con el mail
                       $user_password la contraseña"""
        self.get_info_from_database(id)    
        self.user_number = self.user[0]
        self.user_number = f"{self.user_number}@sistemas.frc.utn.edu.ar"
        self.user_password = self.user[1]
        return self.user_number, self.user_password 




