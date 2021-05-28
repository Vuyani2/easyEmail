import smtplib





s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'vuyanikunelisi@gmail.com'
receiver_email_id = 'vuyanikunelisi@gmail.com'
password = input("Enter senders email password")
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent
message = "hi guys how are you. i am doing fine\n"
message = message + "How was your task yesterday"
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()






