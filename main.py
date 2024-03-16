import string
import random
import platform
import os
from time import sleep

title = '''
\033[1;31m███████╗ \033[1;32m██████╗   \033[1;33m██████╗ 
\033[1;31m██╔════╝ \033[1;32m██╔══██╗ \033[1;33m██╔════╝ 
\033[1;31m███████╗ \033[1;32m██████╔╝ \033[1;33m██║  ███╗
\033[1;31m╚════██║ \033[1;32m██╔═══╝  \033[1;33m██║   ██║
\033[1;31m███████║ \033[1;32m██║      \033[1;33m╚██████╔╝
\033[1;31m╚══════╝ \033[1;32m╚═╝       \033[1;33m╚═════╝ 
\033[1;36mSecure   Password Generator
\033[0m'''


def collect_data():
    
    long = input("How long the password (Defualt:12)? ")

    if long == "":
            long = 12

    elif long.isnumeric():
        long = int(long)
        if long <= 7:
            print("Too Week! use defualt or edit it to something more than 8")
            return collect_data()
    else:
        print("You didn't type an intger! try again.")
        return collect_data()
    
    while True:
        symbols = input("Include symbols? (y/n) ")
        if symbols not in {"y", "n"}:
            print("Wrong value! Try again.")
        else:
            symbols = "yes" if symbols == "y" else "no"
            break

    while True:
        digits = input("Include digits? (y/n) ")
        if digits not in {"y", "n"}:
            print("Wrong value! Try again.")
        else:
            digits = "yes" if digits == "y" else "no"
            break

    print("\nSummaraize:")
    print("length:", long)
    print("include Symbols:", symbols)
    print("include digits:", digits)

    while True:
        submite = input("\nSubmite and generate the password? (y/n) ")
        if submite not in {"y", "n"}:
                print("Wrong value! Try again.")
        else:
            submite = "yes" if submite == "y" else "no"
            break
    
    if submite == "yes":
         return [long, symbols, digits]
    else:
         print("Full them again")
         return collect_data()


def generate_password(length, include_symbols, include_digits):
    symbols_list = [ '@', '#', '$', '&']

    if include_digits == "yes":
        lists = string.ascii_uppercase + string.digits + string.ascii_lowercase
    else:
        lists = string.ascii_uppercase + string.ascii_lowercase

    if include_symbols == "yes":
        symbols_str = ''.join(symbols_list)
        lists += symbols_str

    password = ''.join(random.choice(lists) for _ in range(length))
    return password

def copy2clipboard(text):
    if platform.system() == "Linux" :

        if os.getenv('WAYLAND_DISPLAY'):
            os.system(f'echo "{text}" | wl-copy')

        else:
            os.system(f'echo "{text}" | xclip -selection clipboard')

    elif platform.system() == "Darwin":
        os.system(f'echo "{text}" | pbcopy')

    elif platform.system() == "Windows":
        os.system(f'echo "{text}" | clip')

def save2csv(text):
    lable = input("add a lable to this password: ")
    with open('passwords.csv', 'a') as file:
        file.write(f'"{lable}", "{text}"\n')

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        # For Windows
        os.system('cls')
    else:
        # For Unix-like systems (Linux, macOS)
        os.system('clear')

def main():
    # main function
    print(title)

    length, symbols, digits = collect_data()  # Assuming collect_data returns these values
    password = generate_password(length, symbols, digits)
    print("Generated Password:", password)

    while True:
        copy = input("Copy Generated Password to clipboard? (y/n) ")
        if copy not in {"y", "n"}:
            print("Wrong value! Try again.")
        else:
            copy = "yes" if copy == "y" else "no"
            break

    if copy == 'yes':
        copy2clipboard(password)

    while True:
        save = input("save to the csv file? (y/n) ")
        if save not in {"y", "n"}:
            print("Wrong value! Try again.")
        else:
            save = "yes" if save == "y" else "no"
            break

    if save == 'yes':
        save2csv(password)

    while True:
        q = input("generate other password? (y/n) ")
        if q not in {"y", "n"}:
            print("Wrong value! Try again.")
        else:
            q = "yes" if q == "y" else "no"
            break

    if q == 'yes':
        clear_screen()
        main()
    else:
        print("Have a good day!")
        sleep(3)
        exit()

if __name__ == "__main__":
    main()
