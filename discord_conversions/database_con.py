# Update your python to any version 3.6.x 
# Do pip3 install PyMySQL

import pymysql 

# Information - Database is being hosted on heliohost.org
# These are the connection arguments :
# ricky.heliohost.org - database host
# mrbean_admin - database user
# admin123 - user password
# mrbean_chatbot - database table name


def db_insert(user_id, name, age, height, weight):
    
    con = pymysql.connect("ricky.heliohost.org", "mrbean_admin", "admin123", "mrbean_chatbot")
    cursor = con.cursor()

    cursor.execute("SELECT VERSION()")
    db_version = cursor.fetchone()

    # sql_insert inserts data in the database if the user is having a conversation with the bot for the first time

    sql_insert = "INSERT INTO user(user_id, name, weight, height, age) VALUES (%s, %s, %s, %s, %s);"

    try:
        user_data = (user_id, name, weight, height, age)
        cursor.execute(sql_insert, user_data)
        con.commit

    except IOError as e:
        print(e)
        con.rollback

    con.close()
    return print("Database version: %s " % db_version)

        
    
def db_search(user_id):
    con = pymysql.connect("ricky.heliohost.org", "mrbean_admin", "admin123", "mrbean_chatbot")
    cursor = con.cursor()

    # sql_search retrieves data from the database if the user is an existing user
    sql_search = "SELECT * FROM user WHERE user_id=%s"

    try:
        cursor.execute(sql_search, user_id)
        data = cursor.fetchone()
        if data != None:
            db_search.existing_user = True
            db_search.name = data[1]
        else:
            db_search.existing_user = False
            
    except IOError as e:
        print(e)
        con.rollback()
    

    con.close()