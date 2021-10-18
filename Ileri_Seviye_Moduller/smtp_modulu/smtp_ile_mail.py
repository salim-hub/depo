import smtplib
from email.mime.multipart import MIMEMultipart  # Mesaj gövedesini mail yapısını oluşturacak
from email.mime.text import MIMEText            # Maile ne yazılacağını bu sınıfta oluşturup yazacağız.
from sifre import password
import sys


mesaj = MIMEMultipart()

mesaj["From"] = "karsanbassalim@gmail.com"

mesaj["To"] = "salimkarsanbas@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = """

smtp ile mail gönderiyorum

Salim Karşanbaş

"""

mesaj_govdesi = MIMEText(yazi, "plain") # normal mesaj olduğunu belirtmek için plain.

mesaj.attach(mesaj_govdesi) #mesaj gövdesine atmak için


# GMAIL SERVER INA BAĞLANMAK İÇİN:

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)  #server ve portu.
    mail.ehlo()     # server a bağlanmak için
    mail.starttls() # kullanıcı adı ve şifrelerin şifrelenmesi için

    mail.login("karsanbassalim@gmail.com", password)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

    print("Mail Başarıyla Gönderildi!..")
    
    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()



