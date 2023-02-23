from Database import dbModels,query,db
from Views import register
import mainWindow
import tkinter
import controller
from Config import config


def login(username, password):
    model = dbModels.login(username, password)
    status, log = query.auth(model, db)
    if(status ==1):
        if(log):
            print("Logged in")
            userDetails = {'status':True,'username':username}
            config.saveUser(userDetails)
            return(True)
        else:
            print("Incorrect Credentials")
            return(False)
    else:
        print("Error logging In")
        return(False)

def register(username,fullname,email,password):
    model = dbModels.register(username,fullname,email,password)
    status= query.register(model,db)
    if(status ==1):
        print('registered')
        return True
    else:
        print("Error registering")
        return False

if __name__ == '__main__':
    mainWindow.window(controller)

    
