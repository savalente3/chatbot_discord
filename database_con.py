# Update your python to any version 3.6.x 
# Do pip3 install PyMySQL

import pymysql 

# Information - Database is being hosted on heliohost.org
# These are the connection arguments :
# ricky.heliohost.org - database host
# mrbean_admin - database user
# admin123 - user password
# mrbean_chatbot - database table name

#bot = commands.Bot(command_prefix = '*')
#salute_list = ['Hello', 'hello', 'hi', 'Hi']

name = ""
age = 0
height = 0
weight = 0

'''
@bot.event
async def on_ready():
	print("Have no fear, Chappie is here!")
	print("My user name is " + bot.user.name)
	print("My bot user id is " + bot.user.id)


@bot.event
async def on_message(message):
    if "hello" in message.content:
        await bot.send_message(message.channel, "Hello, my name is GHP. I hope you are willing to share your information with me. What is your name?")
        name  = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "What is your weight?")
        weight = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "What is your height?")
        height = await bot.wait_for_message(author = message.author)
        await bot.send_message(message.channel, "How old are you?")
        age = await bot.wait_for_message(author = message.author)'''

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
    except:
        print("horrible error")
        con.rollback()



    con.close()
    return print("Database version: %s " % data)
#bot.run("NTA2OTgzMDY1NTUwMzIzNzIy.DsEzyg.WzxYWzRFJxxxnuABTNU8Vo8tmLk")