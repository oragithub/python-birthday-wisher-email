import os,pandas,random,datetime as dt,smtplib

FROM_EMAIL = 'Your email from which emails are to be sent'
PASSWORD = 'Your app password of above email account(e.g. For Gmail you can get the app password from gmail settings)'

#datetime now
current_date = dt.datetime.now()
month = current_date.date().month
day = current_date.date().day

#Read birthdays csv file
birthday = pandas.read_csv("birthdays.csv")
to_send_dict = {row['name']:row['email'] for (index,row) in birthday.iterrows() if row.day==day and row.month==month}

#Get random letters from letter folder and send email
all_letters = os.listdir("letter_templates")
for (name,email) in to_send_dict.items():
    letter_name = random.choice(all_letters)
    to_email = email
    with open(f"letter_templates/{letter_name}", mode='r') as letter:
        to_send_letter = letter.read().replace('[NAME]',name)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(to_addrs=to_email, from_addr=FROM_EMAIL, msg=f"Subject:Birthday Wishes :) :)\n\n{to_send_letter}")
    print(f"Sent Birthday wishes to {name}")











