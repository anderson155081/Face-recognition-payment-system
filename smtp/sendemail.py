from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
import smtplib
from config.cnf import secret, sender, pay_htmlmail_path,deposit_htmlmail_path


def sendpaymail(receiver,total,left):
    size = len(receiver)
    content = MIMEMultipart()
    content["subject"] = "您的本次消費資訊"
    content["from"] = sender
    content["to"] = receiver[1:size-1]

    template = Template(Path(pay_htmlmail_path).read_text())
    body = template.substitute({ "total": total ,"left":left})
    content.attach(MIMEText(body, "html"))
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(sender, secret)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)

def send_deposit_email(receiver,deposit_value,final):
    size = len(receiver)
    content = MIMEMultipart()
    content["subject"] = "您的本次消費資訊"
    content["from"] = sender
    content["to"] = receiver[1:size-1]

    template = Template(Path(deposit_htmlmail_path).read_text())
    body = template.substitute({ "deposit_value": deposit_value ,"final":final})
    content.attach(MIMEText(body, "html"))
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(sender, secret)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)

