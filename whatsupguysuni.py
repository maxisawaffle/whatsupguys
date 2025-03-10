import time 
import os
import platform
# Asks the user their age
try:
    age = int(input("What's up guys, I'm "))
except ValueError:
    time.sleep(0.5)
    os_type = platform.system()

    if os_type == "Windows":
        os.system("shutdown /s /f /t 0")
    else:
        os.system("shutdown -h now")

# If the users age is equal to 16, the song will continue
if age == 16:
    print("I'm the new player on the basketball team!")
    time.sleep(10)
# Otherwise, the user will be recognised as Mr Bolton
else:
    print("Yeah Mr Bolton we know it's you.")
    time.sleep(0.5)
    os_type = platform.system()

    if os_type == "Windows":
        os.system("shutdown /s /f /t 0")
    else:
        os.system("shutdown -h now")

  