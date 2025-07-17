unconfirmed_users = ['fred','charles','kaloki']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)
print("\nThe following users have been verified:")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()}")