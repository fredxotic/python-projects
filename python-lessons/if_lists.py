current_users = ['Fred','Charles','Victor','Lillian','Ethan']

user = input("Please Enter your username: ")
if user.title() in current_users:
    print(f"Sorry but username {user}, is already taken.\n")
else:
    print(f"Username {user}, is available.\n")