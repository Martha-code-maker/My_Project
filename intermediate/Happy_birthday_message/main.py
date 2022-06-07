import datetime as dt
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText


my_email = "#"
password = "#"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {
    (data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()
}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    number = random.randint(1,3)
    with open(f'./letter_templates/letter_{number}.txt') as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.naver.com", 587) as connection:
            title = "Happy Birthday!"
            content = contents

            message = MIMEText(content)
            message['From'] = my_email
            message['To'] = birthdays_dict[(today_month,today_day)]["email"]
            message['Subject'] = title

            connection.starttls()
            connection.login(user="#", password=password)
            connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday_person["email"],
                    msg=message.as_string()
            )




