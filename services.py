import smtplib


def send_mail(user, start_time, end_time, room):
    # TODO input your email and password
    FROM = 'test@gmail.com'
    pwd = '12345678'
    if user is not None and room is not None:
        user_username = user[0]
        user_email = user[1]

        message = f"""{user_username} informs you that you have occupied {room[0]} from {start_time} to {end_time}."""
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(FROM, pwd)
            server.sendmail(FROM, user_email, message)
            server.close()
            print('Successfully sent the mail')
        except:
            print("Failed to send mail")
