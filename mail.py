import smtplib
import pymysql.cursors
import re
BDM="Happy birthday to a valued employee whose contribution to the company is worth noticing. \n" \
    "Sincerely, \n" \
    "HR"
ANIVM='Congratulations! Thanks to you, we’re leaders. \n' \
      'At your career milestone, we honor you for the part you play in maintaining our performance standards and commitment to excellence. \n' \
      'Breakthroughs come after spending what seem like hours of hard work and trying new ideas. \n' \
      'We applaud your performance with the attractive recognition \n' \
      'We hope you will select one that you’ll use often in the coming years and thanks for your contributions. \n' \
      'Sincerely, \n ' \
      'HR'
BDM = BDM.encode()
ANIVM = ANIVM.encode()
# Connect to the database.
# Connect to the database.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='teamgnc')
BDMailinglist = []
ANIVMailinglist = []
print("connect successful!!")
try:

    with connection.cursor() as cursor:
        # SQL
        sql = "select email from empgnc where DAY(DOB)=DAY(CURDATE()) && MONTH(DOB)=MONTH(CURDATE());"
        # Execute query.
        cursor.execute(sql)
        for row in cursor:
            row = ''.join(row)
            row = row.rstrip('(),')
            row = row.lstrip('(),')
            row = row.strip()
            BDMailinglist.append(row)


    with connection.cursor() as cursor1:
        # SQL
        sql = "select email from empgnc where DAY(DOJ)=DAY(CURDATE()) && MONTH(DOJ)=MONTH(CURDATE());"
        # Execute query.
        cursor1.execute(sql)
        for row in cursor1:
            row = ''.join(row)
            row = row.rstrip('(),')
            row = row.lstrip('(),')
            row = row.strip()
            ANIVMailinglist.append(row)

finally:
    # Close connection.
    connection.close()


def mailauto():
    if (BDMailinglist!=[] or ANIVMailinglist !=[]):
        if(BDMailinglist!=[]):

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("hr.teamgnc@gmail.com", "hackshetra")
            for key in BDMailinglist:
                server.sendmail("hr.teamgnc@gmail.com", key, BDM)
            print("Birthday mails have been sent to IDs \n")
            for key in BDMailinglist:
                print(key)
            BDMailinglist.clear()
        if (ANIVMailinglist != []):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("hr.teamgnc@gmail.com", "hackshetra")
            for key in ANIVMailinglist:
                server.sendmail("hr.teamgnc@gmail.com", key, ANIVM)
            print("Anniverssary mails have been sent to IDs\n")
            for key in ANIVMailinglist:
                print(key)
        ANIVMailinglist.clear()
    # server.quit()

mailauto()
print("\nThe Emails have been sent");