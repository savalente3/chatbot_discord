# Update your python to any version 3.6.x 
# Do pip3 install PyMySQL
# This only works locally for now - code will be improved in future

import pymysql 

# These are the connection arguments :
# 127.0.0.1 - database server
# admin - database user
# admin123 - user password
# user - database table name

name = "mariazinha"
weight = 23
height = 123
age = 27

con = pymysql.connect("127.0.0.1", "admin", "admin123", "user")
cursor = con.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

# This is the sql code that will be executed

sql = "INSERT INTO user(name, weight, height, age) \
		VALUES ('%s', '%d','%d', '%d')" % \
		( name, weight, height, age)


try:
	cursor.execute(sql)
	con.commit()

except:
	con.rollback()


print("Database version: %s " % data)

con.close()
