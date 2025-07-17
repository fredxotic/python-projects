username = input("Enter your username: ").lower()
password = input("Enter your password: ")
if username == "fred".lower():
    if password == "Fred16807.":
        print("Welcome Fred!")
    else:
        print("Incorrect password.")
else:
    print("user not found.")
# The above code is a simple login system that checks the username and password.
