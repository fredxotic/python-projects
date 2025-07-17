def city_country(city, country):
    unformatted_string = f"{city} {country}"
    return unformatted_string.title()

while True:
    print("\nPlease enter the city and country:")
    city = input("City: ")
    country = input("Country: ")

    formatted_strings = city_country(city, country)
    print(f"\n{formatted_strings}")
