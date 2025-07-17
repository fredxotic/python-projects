from pathlib import Path

while True:
    user = input("Enter your name: ")
    print("Saving your Data.")
    user_input = print("Do you widh to add any other name (yes/no): ")
    if user_input == 'yes':
        continue
    else:
        break
    

path = Path('Practice_File.txt')
path.write_text(user)


