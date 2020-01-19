import json
<<<<<<< HEAD
with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)
for i in jsonData:
    
=======
import smtplib, ssl

#with open('') as json_data:
    #jsonData = json.load(json_data)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "testemailerpy@gmail.com"  # Enter your address
receiver_email = "cameronohare.98@hotmail.co.uk"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
>>>>>>> 251951c2f6209c8916453caf763ca34ec6a4b534
    