import mysql.connector as con

host = 'localhost'
user = 'root'
password = '20441988'
try:
    db = con.connect(host = host, user = user, password = password)
    print('database connected')
except Exception as e :
    print(e)

def getDb():
    return(db)