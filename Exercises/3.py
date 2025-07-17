numbers = int(input("Enter a number: "))
dictionary_of_numbers = dict()

for number in range(1, numbers + 1):
    dictionary_of_numbers[number] = number * number

print(dictionary_of_numbers)