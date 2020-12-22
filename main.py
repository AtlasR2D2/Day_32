import smtplib
import datetime as dt
import pandas as pd
import random

email_smtp = {
    "Gmail": "smtp.gmail.com",
    "Hotmail": "smtp.live.com",
    "Outlook": "outlook.office365.com",
    "Yahoo": "smtp.mail.yahoo.com"
}

my_email = "day31.testing.1@gmail.com"
my_email_provider = my_email[my_email.find("@")+1:my_email.find(".com", my_email.find("@"))].title()
password = "testingTESTING1212"

SUBJECT = "HAPPY BIRTHDAY !!!"

##################### Extra Hard Starting Project ######################


# 1. Update the birthdays.csv
# Done - or update as appropriate
birthdays_df = pd.read_csv("birthdays.csv")
birthdays_df["Birthday"] = list(zip(birthdays_df["month"], birthdays_df["day"]))

#2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now().date()
df_filter = (birthdays_df["Birthday"] == (today.month, today.day))
birthdays_today_df = birthdays_df[df_filter]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(birthdays_today_df) > 0:
    # There exists at least one person with today as their birthday
    for ix, row in birthdays_today_df.iterrows():
        birthday_person = row['name']
        email_recipient = row['email']
        letter_choice = "letter_" + str(random.randint(1, 3)) + ".txt"

        with open("./letter_templates/"+letter_choice, "r") as letter:
            letter_text = letter.read()
            letter_text = letter_text.replace("[NAME]", birthday_person.title())

# 4. Send the letter generated in step 3 to that person's email address.

        email_msg = f"Subject:{SUBJECT}\n\n{letter_text}".encode("utf-8")

        with smtplib.SMTP(email_smtp[my_email_provider]) as connection:
            connection.starttls()
            connection.login(user=my_email,
                             password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_recipient,
                                msg=email_msg)
