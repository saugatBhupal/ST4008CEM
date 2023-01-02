class login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def getUsername(self):
        return(self.username)
    def getPassword(self):
        return(self.password)

class register:
    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email
        
    def getUsername(self):
        return(self.username)
    def getPassword(self):
        return(self.password)
    def getEmail(self):
        return(self.email)
