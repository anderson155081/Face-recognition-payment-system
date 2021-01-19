import mysql.connector
from mysql.connector import errorcode
from smtp.sendemail import sendpaymail
from config.cnf import DB_config

Name = input()
total = int(input())

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

    cursor.execute("SELECT money FROM Costumer_info WHERE name = %s;",(Name,))
    current_money = cursor.fetchall()
    res = str(current_money[0]).replace('(','').replace(')','').replace(',','')
    current_money = int(res)
    left_money = current_money - total

    if left_money<0:
        print("Money not enough, please charge")
    else:
        cursor.execute("UPDATE Costumer_info SET money = %s WHERE name = %s;",(left_money,Name))
    
    cursor.execute("SELECT email FROM Costumer_info WHERE name = %s;",(Name,))
    mail = cursor.fetchall()
    email = str(mail[0]).replace('(','').replace(')','').replace(',','')

    cnx.commit()
    cursor.close()
    cnx.close()
    print("Done.")

    sendpaymail(email,total,left_money)
    print("mail send")
