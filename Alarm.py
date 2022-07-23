import datetime as dt
from playsound import playsound
import os

hr, min = input("Set your alarm, Please enter your time in 'hh/mm' format").split("/")

hr, min = int(hr), int(min)

am_pm = str(input("am or pm?").lower())

if am_pm == "pm":
    hr = hr + 12

if am_pm == "am" and hr == 12:
    hr = hr - 12

while True:
    if hr == dt.datetime.now().hour and min == dt.datetime.now().minute:
        print("hey user please wake up")
        os.chdir("C:\Windows\Media")
        playsound("Alarm07.wav")
        break
