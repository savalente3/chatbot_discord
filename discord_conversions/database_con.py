# Update your python to any version 3.6.x 
# Do pip3 install PyMySQL

import pymysql 

# Information - Database is being hosted on heliohost.org
# These are the connection arguments :
# ricky.heliohost.org - database host
# mrbean_admin - database user
# admin123 - user password
# mrbean_chatbot - database table name


def db_con(name, age, height, weight):
    
    con = pymysql.connect("ricky.heliohost.org", "mrbean_admin", "admin123", "mrbean_chatbot")
    cursor = con.cursor()

    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()

    # This is the sql code that will be executed

    sql = "INSERT INTO user(name, weight, height, age) VALUES ('%s', '%d', '%d', '%d');"

    #check online how to handle except errors, I am getting an error but need to  know what error it is
    try:
        cursor.execute(sql, (name,weight,height,age))
        con.commit()
    except(RuntimeError, TypeError, NameError):
        pass
        print("horrible error")
        con.rollback()



    con.close()
    return print("Database version: %s " % data)

        
    
    
    '''con = pymysql.connect("ricky.heliohost.org", "mrbean_admin", "admin123", "mrbean_chatbot")
    cursor = con.cursor()

    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()

    # This is the sql code that will be executed

    sql = "INSERT INTO user(name, weight, height, age) VALUES ('%s', '%d', '%d', '%d');"

    #check online how to handle except errors, I am getting an error but need to  know what error it is
    try:
        cursor.execute(sql)
        con.commit()
    except(RuntimeError, TypeError, NameError):
        pass
        print("horrible error")
        con.rollback()



    con.close()
    return print("Database version: %s " % data)'''


'''

def db_con(name, age, height, weight):
    con = pymysql.connect("ricky.heliohost.org", "mrbean_admin", "admin123", "mrbean_chatbot")
    cursor = con.cursor()

    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()

    # This is the sql code that will be executed

    sql = "INSERT INTO user(name, weight, height, age) VALUES (%s, %d, %d, %d);"

    #check online how to handle except errors, I am getting an error but need to  know what error it is
    try:
        cursor.execute(sql, (name,weight,height,age))
        con.commit()
    except(RuntimeError, TypeError, NameError):
        pass
        print("horrible error")
        con.rollback()



    con.close()
    return print("Database version: %s " % data)


'''