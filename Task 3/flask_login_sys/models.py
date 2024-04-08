from flask_login import UserMixin

from data_helper import get_user, insert_user

# Mocked user data
class User(UserMixin):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def is_authenticated(self):

        flag = get_user(self.email, self.password)

        if flag == 1:

            return True
        
        else:

            return False
        
    def is_anonymous(self):

        if self.is_authenticated():

            True
        
        else:

            False

    def get_id(self):

        return str(self.email)


