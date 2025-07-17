from pathlib import Path
import json

path = Path('user_number.json')
contents = path.read_text()
user_number = json.loads(contents)

print(user_number)