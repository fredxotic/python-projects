while True:
    try: 
        first_num = input("Enter a number: ")
        second_num = input("Enter another number: ")
        results = int(first_num) + int(second_num)
        print(f" {first_num} + {second_num} =", results)

    except ValueError:
        print("Please enter a valid number!\n")