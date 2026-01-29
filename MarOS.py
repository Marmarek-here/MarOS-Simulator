from datetime import datetime
import time
import sys
import os
import random as ran
installationPrompt = input("Hello, this is MarOS installer. You will go through the installation and be ready to use the OS itself. Y/n: ")
while installationPrompt == "Y" or installationPrompt == "y":
    username = input("Enter your name (e.g John Johnson): ")
    diskChosen = input("Select a disk: (e.g, /dev/sdXnY):")
    confirm = input("Are you sure you want to install to disk " + diskChosen + "? Y/n: ")
    if confirm == "Y" or confirm == "y":
        break
if installationPrompt.lower() != "y":
    print("Installation aborted.")
    exit()
print("Installing MarOS to " + diskChosen + " in 3... 2... 1...")
steps = [
    "Formatting disk...",
    "Extracting kernel and bootloader...",
    "Setting up shell and command environment...",
    "Creating user...",
    "Cleaning up temporary files..."
]

bar_length = 20

for step in steps:
    print(step)
    for i in range(21):
        percent = i * 5
        fill_length = i
        empty_length = bar_length - fill_length
        bar = "#" * fill_length + "*" * empty_length
        mid = bar_length // 2 - len(f"{percent}%") // 2
        bar_with_percent = bar[:mid] + f"{percent}%" + bar[mid+len(f'{percent}%'):]
        sys.stdout.write(f"\r[{bar_with_percent}]")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\n")
    time.sleep(0.5)
print("Installation complete! Please restart your computer to use MarOS.")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
print("Hello!")
isBooted = True
time.sleep(3)
while isBooted == True:
    command = input(username + "@MarOSCommandPromptEnvironment:~$: ")
    if command == "help":
        print("Available commands: version; help; echo; shutdown; restart; date; ls; whoami; cls; guess; math. ")
    elif command == "version":
        print("MarOS v1.0-pb using GNU/Linux kernel with version 6.18.7-105-lts for x86_64 and arm64-v8 architecture.")
    elif command.startswith("echo "):
        toEcho = command[5:]
        print(toEcho)
    elif command == "shutdown":
        print("Shutting Down...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    elif command == "restart":
        print("Restarting...")
        isBooted = False
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        isBooted = True
        print("Hello!")
    elif command == "date":
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print("Current date and time: ", current_time)
    elif command == "ls":
        print("Desktop   Documents  Downloads  Music  Pictures  Videos  User")
    elif command == "whoami":
        print(username)
    elif command == "cls":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif command == "guess":     
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        choice = int(input("Choose a number out of 1 to 10 (e.g. 6): "))
        result = ran.choice(numbers)
        if choice == result:
            print(f"PC chose {result}, so you won!")
        if choice != result:
            print(f"PC chose {result}, so you lost.")
    elif command == "math":
        x = int(input("Type the first number: "))
        y = int(input("Type the second number: "))
        op = input("Do you want to add (+), subtract (-), multiply (*) or divide (/)?")
        if op == "+":
            do = x + y
        elif op == "-":
            do = x - y
        elif op == "*":
            do = x * y
        elif op == "/":
            if y == 0:
                print("You cannot divide by zero in math. Or in college maybe, just maybe, sometimes.")
                continue
            do = round(x / y, 2)
        else:
            print("Unknown operator or number.")
        print(f"{x} {op} {y} equals {do}.")
    else:
        print(f"bash: {command}: Command not found. Type 'help' to see available commands.")