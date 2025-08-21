def km_to_mile(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles/ 0.621371

def c_to_f(celcius):
    return (celcius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("🌏 Unit Conventer")
print("1. Kilometeres to mile")
print("2. Miles to Kilometeres")
print("3. Celcius to Fahrenheit")
print("4. Fahrenheit to Celcius")

choice = input("Choose conversion (1 -4), Enter (Q) to quit or (B) to go back: ")

try:
    while True:
        if choice == 'Q':
            break

        if choice == 'B':
            choice = input("Choose conversion (1 -4), Enter (Q) to quit or (B) to go back: ")

        if choice == '1':
            km = float(input("Enter Kilometers: "))
            print(f"{km} km = {km_to_mile(km):.2f}miles")

        elif choice == '2':
            miles = float(input("Enter miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f}km")

        elif choice == '3':
            celcius = float(input("Enter Celsius: "))
            print(f"{celcius}°C = {c_to_f(celcius):.2f}°F")

        elif choice == '4':
            fahrenheit = float(input("Enter the fahrenheit: "))
            print(f"{fahrenheit}°F = {f_to_c(fahrenheit):.2f}°C")

        else:
            print("❌ Invalid choice.")
            break

except ValueError:
    print("❌ Please enter a valid number.")