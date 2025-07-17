# Step 1: Create a guest list
guests = ["Alice", "Brian", "Cynthia"]

# Step 2: Send invitations
for guest in guests:
    print(f"Hi {guest}, you're invited to dinner!")

# Step 3: Cynthia can't make it
print("\nCynthia can't make it to dinner.")
guests[2] = "David"  # Replace Cynthia with David

# Step 4: Re-send updated invitations
for guest in guests:
    print(f"Hi {guest}, you're still invited to dinner!")

# Step 5: Check if "John" is invited
if "John" in guests:
    print("\nJohn is on the guest list.")
else:
    print("\nJohn is not on the guest list.")
