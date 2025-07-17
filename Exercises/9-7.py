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

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.priviliege = ['can add post','can delete post','can ban user','can add members','can assign menbers to be admin']

    def show_privileges(self):
        print("Only Admins can do the following:")
        for priviledge in self.priviliege:
            print(f"\t{priviledge.title()}")

admin_1 = Admin('Monicah','Wanjiru',18,'kenya')
print(admin_1.describe_user())
admin_1.show_privileges()
    