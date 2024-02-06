import smtplib
import pandas as pd
import datetime as dt
import random

today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Load the data
data = pd.read_csv('birthdays.csv')
sendAddress = data['email'][1]

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Set up the SMTP server
MY_ADDRESS = "basilisgim4@gmail.com"
PASSWORD = "yfcbcaqgmmxxxfna"

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_ADDRESS, PASSWORD)
        connection.sendmail(
            from_addr=MY_ADDRESS,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )




