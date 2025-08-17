#Admin authentication
class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "admin@123"
        
    def login(self, user, pw):
        return user == self.username and pw == self.password

