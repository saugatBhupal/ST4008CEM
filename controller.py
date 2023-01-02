from Database import dbModels,query,db
from Views import register
import mainWindow
import tkinter
import controller


def login(username, password):
    login = dbModels.login(username, password)
    status, log = query.auth(login,db)
    if(status ==1):
        if(log):
            print("Logged in")
            return(True)
        else:
            print("Incorrect Credentials")
            return(False)
    else:
        print("Error logging In")
        return(False)
    
if __name__ == '__main__':
    mainWindow.window(controller)

    
