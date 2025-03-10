import time 
import os
# Asks the user their age
age = int(input("What's up guys, I'm "))
#If the users age is equal to 16, the song will continue
if age == 16:
    print("I'm the new player on the basketball team!")
    time.sleep(10)
# Otherwise, the user will be recognised as Mr Bolton
else:
    print("Yeah Mr Bolton we know it's you.")
    time.sleep(1.5)
    os.system("shutdown /s /f /t 0")
    # Shuts down the system to represent the gun firing in the original song.
    