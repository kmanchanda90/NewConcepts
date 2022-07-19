from smtplib import SMTP

server = SMTP('smtp.gmail.com', 587)

server.starttls()

server.ehlo()

server.login("drakepy7@gmail.com", "gefovlpfxbsncede")

server.sendmail('drakepy7@gmail.com', 'karanmanchanda90@gmail.com', "Hey! It's cool. We tried email automation for "
                                                                    "the first time")
server.close()

print("Mail sent")

