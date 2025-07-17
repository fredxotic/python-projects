from pathlib import Path
import json

def get_stored_users(path):
    if path.exists():
        contents = path.read_text()
        users = json.loads(contents)
        return users
    else:
        return {}

def get_user_info():
    username = input("What is your username? ")

    age = input("How old are you? ")
    favorite_color = input("What is your favorite color? ")

    return username, {
        "age": age, 
        "favorite_color": favorite_color
    }                                                                    

def greet_user():
    path = Path("users.json")
    users = get_stored_users(path)

    username = input("Enter your username: ")

    if username in users:
        user_info = users[username]
        print(f"Welcome back, {username}!")
        print(f"We remember that you are {user_info['age']} years old and your favorite color is {user_info['favorite_color']}.")
    else:
        print("We don't know you yet. Let's get your info.")
        age = input("How old are you? ")
        favorite_color = input("What is your favorite color? ")

        users[username] = {
            "age": age,
            "favorite_color": favorite_color
        }

        path.write_text(json.dumps(users))
        print(f"We'll remember you when you come back, {username}!")

greet_user()
