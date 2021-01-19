import mysql.connector
from mysql.connector import errorcode
from smtp.sendemail import send_deposit_email
from config.cnf import DB_config

name = input()
deposit_value = int(input())

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

    cursor.execute("SELECT money FROM Costumer_info WHERE name = %s;",(name,))
    current_money = cursor.fetchall()
    res = str(current_money[0]).replace('(','').replace(')','').replace(',','')
    current_money = int(res)
    
    final = current_money + deposit_value

    cursor.execute("UPDATE Costumer_info SET money = %s WHERE name = %s;",(final,name))
    
    cursor.execute("SELECT email FROM Costumer_info WHERE name = %s;",(name,))
    mail = cursor.fetchall()
    email = str(mail[0]).replace('(','').replace(')','').replace(',','')

    cnx.commit()
    cursor.close()
    cnx.close()
    print("Done.")

    send_deposit_email(email,deposit_value,final)
    print("mail send")
