import smtplib
import pymysql.cursors
import re

# Connect to the database.
# Connect to the database.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='teamgnc')
mailinglist = []
# def checkCon:
#     sql1 = "SELECT email FROM empgnc where "
print("connect successful!!")
try:

    with connection.cursor() as cursor:

        # SQL
        sql = "SELECT email FROM empgnc where EID>1000"
        # Execute query.
        cursor.execute(sql)
        for row in cursor:
            row = ''.join(row)
            row = row.rstrip('(),')
            row = row.lstrip('(),')
            row = row.strip()
            mailinglist.append(row)
            print(row)

finally:
    # Close connection.
    connection.close()


def mailauto():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("hr.teamgnc@gmail.com", "hackshetra")
    for key in mailinglist:
            msg = "Hello It's finally working"
            print(key)
            server.sendmail("hr.teamgnc@gmail.com", key, msg)
    server.quit()

mailauto()
