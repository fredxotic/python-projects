def get_formatted_name(first_name, second_name):
    full_name = f"{first_name} {second_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    s_name = input("Second name: ")

    formatted_name = get_formatted_name(f_name, s_name)
    print(f"\nHello, {formatted_name}")
    break