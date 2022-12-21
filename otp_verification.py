import os
import math
import random
import smtplib
from time import sleep
from dotenv import load_dotenv

load_dotenv('.env')

user_email = os.environ.get("EMAIL")
app_pw = os.environ.get('APP_PW')

digits = "0123456789"

OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

otp = OTP + " is your one-time passcode"

msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(user_email, app_pw)

emailid = input("Enter your email: ")

s.sendmail('&&&&&&&&&&&', emailid, msg)
sleep(0.5)
print("Please check your email for your one-time passcode")
sleep(3)

a = input("Enter your one-time passcode >>: ")

if a == OTP:
    print("Verified")

else:
    print("Please check your one-time passcode and try again")
