import smtplib
import email.message



class MailSender:

    def send_mail(self, adress, subject, body):
        user = 'hpspammermail@gmail.com'
        password = 'idruckleicazzate'
        m = email.message.Message()
        m['From'] = "hpspammermail@gmail.com"
        m['To'] = adress
        m['Subject'] = subject
        m.set_payload(body)
        try:
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()
            server_ssl.login(user, password)
            server_ssl.sendmail(user, adress, m.as_string())
            server_ssl.close()
        except:
            print("Error sending mail.")

