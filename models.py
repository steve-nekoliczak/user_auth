
class User(dict):

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def to_dict(self):
        return self.__dict__
