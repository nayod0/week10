from distutils.util import execute
from sqlite3 import DatabaseError
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="week_10"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE week_10")


mycursor.execute("CREATE TABLE Accounts (ID int(11) Primary key AUTO_INCREMENT ,Fullname varchar(100) , Username varchar(100),Password varchar(100), Email varchar(100))")

sql = "INSERT INTO Accounts (ID, fullname, Username, Password, Email ) VALUES (%s, %s, %s, %s, %s)"
val = [
('64160024','Jeeranun Eiei','iceeiei123','iceeiei567', 'ice@gmail.com'),]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")