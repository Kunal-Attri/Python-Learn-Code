# Clear Screen of the terminal while python program execution

# driver code
from os import system, name

def clear():
    # For Linux, Mac, Unix, BSDs, etc
    system('clear')

    # For Windows
    #system('cls')
    # Mine is linux so i am commenting this

# Lets use this
from time import sleep

clear()
for i in range(101):
    print("Processing...", i, "%")
    sleep(0.1)
    clear()

print("Thank you")
sleep(2)


# Thank you...
