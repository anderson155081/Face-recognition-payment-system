import mysql.connector
from mysql.connector import errorcode
from config.cnf import DB_config

name = input()
phone = input()
mail = input()
money = input()


try:
    cnx = mysql.connector.connect(**DB_config)
    print("Connection established")
except mysqll.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = cnx.cursor()

    cursor.execute("INSERT INTO Costumer_info(name, phone, email, money) VALUES (%s,%s,%s,%s);", (name, phone, mail, money))
    print("Inserted", cursor.rowcount, "row(s) of data.")

    cnx.commit()
    cursor.close()
    cnx.close()
    print("Done.")