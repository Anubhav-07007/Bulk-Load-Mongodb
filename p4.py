import mysql.connector as connection

mydb=connection.connect(host="localhost",user="root",passwd="ar@66007")

print(mydb)

cursor=mydb.cursor()
#cursor.execute("use anubhav")

cursor.execute(" LOAD DATA INFILE 'D:\\mysql\\data fsds -20220724T095124Z-001\\data fsds\bank_full.csv',
INTO TABLE bank_full1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;")


coalesce ('29/8/2013',0)+ coalesce ('31/8/2013',0) + coalesce( '2013-02-09 00:00:00',0)+ coalesce ('2013-04-09 00:00:00',0) + coalesce('2013-06-09 00:00:00',0) + coalesce('2013-08-09 00:00:00',0) + coalesce('2013-10-09 00:00:00',0) + coalesce('2013-12-09 00:00:00',0)+ coalesce(' 14/9/2013',0) + coalesce(' 16/9/2013',0)+ coalesce ('18/9/2013',0) + coalesce('20/9/2013',0) + coalesce('22/9/2013',0)+ coalesce(' 24/9/2013',0) + coalesce( '28/9/2013',0) + coalesce ('2013-06-10 00:00:00',0) + coalesce( '2013-12-10 00:00:00',0)) AS Total_Sales FROM dress AS s GROUP BY s.Dress_ID Order by Total_Sales desc;