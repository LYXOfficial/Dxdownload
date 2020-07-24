import smtplib
from email.mime.text import MIMEText
import os
def mail(c="test",t="test"):
    mail_host = "smtp.qq.com"
    mail_user = "2192016328"
    mail_pass = "otajylyopkfediaf"
    sender = '2192016328@qq.com'
    receivers = ['cqfl120400qq@outlook.com']
    content = c
    title = t
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
if __name__=="__main__":
    mail()