import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "afridimohamed38@gmail.com"
password = "cqoguyfxeeqmzxhy"

receiver = "afridimohamed38@gmail.com"

message = """\
Subject : test!!
Hi !
How are you?
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
