favorite_language = {
    'Fred':'Python',
    'Charles': 'Rust',
    'Victor': 'C',
    'Lyon': 'C++',
    'Ethan':'Java',
}

for names in favorite_language.keys():
    print(f"Thank you {names.title()}, for taking part in the poll.")
if 'kaloki' or 'mutinda' not in favorite_language.keys():
    print("\nKaloki please take our poll.")
    print("Mutinda please take our poll.")