import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)

conn.ehlo()
conn.starttls()
conn.login('asweigart@gmail.com', 'adhjfajk;shdf;hsd')
conn.sendmail('asweigart@gmail.com','asweigart@gmail.com', 'Subject: So Long...\n\n Dear Al, \nSo Long, and thanks for all the fish.\n\n-Al')
conn.quit()