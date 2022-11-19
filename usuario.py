"""class user"""


class Usuario:
    def __init__(self,id_user=None,username=None,password=None):
        self._id_user = id_user
        self._username = username
        self._password = password
        
        
    def __str__(self):
        return f"values id: {self._id_user} username: {self._username}, password: {self._password}"
        
    @property
    def id_user(self):
        return self._id_user
    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user
        
        
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        self._username = username
        
        
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password
        
        
        
if __name__ == "__main__":
    obj=Usuario("acer","qw12")
    print(obj)
    
    
    
#successful