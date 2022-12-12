from db import getDb
 
def auth(model):
    username = model.getUsername()
    password = model.getPassword()
    cursor = getDb().cursor()
    try:
        cursor.execute(f'select password from magicAi.Users WHERE userName = "{username}"')
        dbPassword = (cursor.fetchone()[0])
        if(dbPassword == password):
            return 1,True
        else:
            return 1,False
        
    except Exception as e:
        print("Error logging in")
        return 0, False
        
   

def register(model):
    username = model.getUsername()
    fullname = model.getFullName()
    email = model.getEmail()
    password = model.getPassword()
    cursor = getDb().cursor()
    try:
        cursor.execute('Insert into magicAi.Users (userName , email , password , fullName) Values("{username}","{email}","{password}", "{fullname}")')
        return 1
    except Exception as e:
        print("Error Registering", e)
        return 0

    
    