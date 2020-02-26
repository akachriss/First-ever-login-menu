import time
import webbrowser

print("Please make an account!")
time.sleep(1.5)
user = input("Make a Username!:")
passw = input("Make a Password!:")
accounts = []
if user in accounts:
    print("Username is already taken")
else:
    accounts.append(user)
    accounts.append(passw)
    print("Username, password:" , accounts)
    time.sleep(2)

def login():
    print("Please login.")
    user = input("Enter username:")
    passw = input("Enter password:")

    if user and passw not in accounts:
        print("Login failed try again.")
        login()
    else:
        print("Login Successful!")
        time.sleep(1.5)
        menu()

def menu():
    print("Welcome to the menu!")
    time.sleep(1)
    safari = "1"
    spotify = "2"
    choice = input("Where would you like to go? 1)Google, 2)Twitter, 3)Youtube (enter number)")
    if choice == "1":
        webbrowser.open("http://google.com")
    elif choice == "2":
        webbrowser.open("http://Twitter.com")
    elif choice == "3":
        webbrowser.open("http://Youtube.com")
    else:
        print("Invalid input")

login()