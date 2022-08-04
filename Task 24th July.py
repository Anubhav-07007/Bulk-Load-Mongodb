import mysql.connector as connection

mydb=connection.connect(host="localhost",user="root",passwd="ar@66007")

print(mydb)

cursor=mydb.cursor()

#cursor.execute("show databases")

#cursor.execute("use anubhav")
#cursor.execute("show tables")

#cursor.execute('select * from anubhav.bank_full')
#for i in cursor.fetchall():

   # print(i)