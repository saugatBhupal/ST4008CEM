def auth(model,db):
    username = model.getUsername()
    password = model.getPassword()
    cursor = db.getDb().cursor()
    status = 1
    log = False
    try:
        cursor.execute(f'select password from magicAi.Users WHERE userName = "{username}" or email = "{username}"')
        dbPassword = (cursor.fetchone()[0])
        if(dbPassword != None):
            if(dbPassword == password):
                print("Auth Success")
                status, log =  1,True
        else:
            print("Auth Failed")
            status, log =  1,False
        
    except Exception as e:
        print("Error logging in (DB)")
        print(e)
        status, log =  0, False
    
    return status, log

def register(model,db):
    username = model.getUsername()
    email = model.getEmail()
    fullname = model.getFullname()
    password = model.getPassword()
    cursor = db.getDb().cursor()
    database = db.getDb()
    try:
        cursor.execute(f'Insert into magicAi.Users (userName , email , password, FullName ) Values ("{username}","{email}","{password}", "{fullname}")')
        database.commit()
        return 1
    except Exception as e:
        print("Error Registering", e)
        return 0

def delete(db, username):
    cursor = db.getDb().cursor()
    try:
        cursor.execute(f'delete from magicAi.Users where username = "{username}"')
        return 1
    except Exception as e :
        print("Error Deleting Account")
        return 0

def updatePassword(db,model):
    username = model.getUsername();
    password = model.getPassword();
    cursor = db.getDb().cursor()
    try:
        cursor.execute(f'update magicAi.Users set password = "{password}" where username = "{username}"')
        return 1
    except Exception as e:
        print('Error Updating Password')
        return 0 