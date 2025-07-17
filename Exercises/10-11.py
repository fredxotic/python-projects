from pathlib import Path
import json

path = Path('user_number.json')

if path.exists():
    contents = path.read_text()
    user_number = json.loads(contents)
    print(f"Your fav number is: {user_number}")

else:
    user_number = int(input("Enter your favourite number: "))
    contents = json.dumps(user_number)
    path.write_text(contents)
    print(f"Your favourite number is {user_number}")