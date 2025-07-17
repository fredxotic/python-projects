class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print("The following are your details:")
        return f"\tName: {self.first_name.title()} {self.last_name.title()}.\n\tAge: {self.age}\n\tCountry: {self.country.title()}"

    def greet_user(self):
        print(f"\tWelcome aboard, {self.first_name.title()} {self.last_name.title()}.")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"\tAttempts to login:",self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("\tRemaining attempts:",self.login_attempts)

user1 = User('Fred', 'Kaloki', '17', 'Kenya')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.reset_login_attempts()