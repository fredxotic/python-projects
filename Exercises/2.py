def factorial_of_number(number):
    if number == 0:
        return 1
    return number * factorial_of_number(number - 1)

number = int(input("Enter a number: "))
print(factorial_of_number(number))
        
