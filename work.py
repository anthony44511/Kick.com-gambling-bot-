import pyautogui
import time
import os

# Clear the console.
os.system("cls")

# Get the message to print and the number of times to print it.
msg = input("Enter the message: ")
n = input("How many times ?: ")

# Print a countdown message.
print("t minus")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# Print the message `n` times.
print("Fire in the hole!!!")
for i in range(0, int(n)):
    pyautogui.typewrite(msg + '\n')
    time.sleep(3)

# Print a message to let the user know that the messages have been sent.
print("Message sent!")