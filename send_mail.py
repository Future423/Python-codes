import smtplib 
from email.message import EmailMessage
email = EmailMessage()
# replace dummy data with original data.
email['from'] = 'dummy_mail'
email['to'] = 'dummy_mail_2'
email['subject'] = 'dummy_subject'
email.set_content("dummy_content") ## content of email
with smtlib.SMTP(host='smtp.gmail.com',port=587)as smtp:     
## sending request to server 
    
smtp.ehlo()          
smtp.starttls()      
smtop.login("email_id","Password") 
smtp.send_message(email)  
# optinal -> print the mail you sent on cmd in case you want to review it.
print("email send")