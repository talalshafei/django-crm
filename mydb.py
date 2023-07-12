import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'talal2002', 
)

# cursorObject = dataBase.cursor()

# cursorObject.execute("CREATE DATABASE elderco")

# print("All done!")