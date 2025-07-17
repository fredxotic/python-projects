#creation of the list of guest
guests = []
guests.append('fred')
guests.append('charles')
guests.append('kaloki')
guests.append('mutinda')

#invitation to the dinner
for guest in guests:
    print(f"Hello, {guest.title()}, you are invited to my dinner.")

#indication that some guest wont come
print("\nMutinda won't be able to attend the dinner")
print("\n")
guests[3] = "David"

#Resending of updated lists
for guest in guests:
    print(f"The dinner still on, {guest} , you are cordially invited.")

#invitation of more guest due to emergence of a bigger table
print("\ni just found a big table for the dinner,adding more guest to the list (: .")

guests.insert(0,'ethan')
guests.insert(3,'victor')
guests.append('lillian')
print("\n")

#RESENDING THE FINAL UPDATED LISTS
for guest in guests:
    print(f"You are lucky {guest.lower()} to be invited to my dinner.")

#sad news that i only can invite two people
print("\nAm sorry guys, but its seems that the table i ordered will arrive late, am updating the list to only two guests.")


#removing the guests that won't be attending the dinner
first_one = "ethan"
guests.remove(first_one)
print(f"\nUnder the circumstances am sorry {first_one.title()} but its seems you won't be attending.")

second_one = "David"
guests.remove(second_one)
print(f"Under the circumstances am sorry {second_one.title()} but its seems you won't be attending.")

third_one = "lillian"
guests.remove(third_one)
print(f"Under the circumstances am sorry {third_one.title()} but its seems you won't be attending.")

fourth_one = "victor"
guests.remove(fourth_one)
print(f"Under the circumstances am sorry {fourth_one.title()} but its seems you won't be attending.")

fifth_one = "charles"
guests.remove(fifth_one)
print(f"Under the circumstances am sorry {fifth_one.title()} but its seems you won't be attending.")
print("\n")

#Sending the final invitation the remainining guests
for guest in guests:
    print(f"Hello, {guest.title()}, it is with great pleasure i invite you to my dinner.")
print("\n")


#Removig all the guets
del guests[0]
del guests[-1]

#Confirming that the guest list is empty
print(guests)

#confirming the number of guests 
len(guests)