# Go to this website for your reference: 
# https://www.quora.com/How-can-I-delete-the-last-printed-line-in-Python-language
# https://stackoverflow.com/questions/5174810/how-to-turn-off-blinking-cursor-in-command-window

import time

day_today = time.strftime("%A, %B %d, %Y")
print("The date today is:", day_today)
time_now = time.localtime

# To hide the cursor:
print('\033[?25l', end="")
 
print("The time now is:")
while True:
    print(time.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)

# You should run this code from the terminal in order to see the time changing in the same output line.

