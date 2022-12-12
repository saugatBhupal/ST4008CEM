import query
class login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def getUsername(self):
        return(self.username)
    def getPassword(self):
        return(self.getPassword)

class register:
    def __init__(self, username, fullname, email, password):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        
    def getUsername(self):
        return(self.username)
    def getPassword(self):
        return(self.getPassword)
    def getFullName(self):
        return(self.fullname)
    def getEmail(self):
        return(self.email)

register = register("man", "man man", "man@abcd.com", "man123")
print(query.register(register))