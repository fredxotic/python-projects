my_dict = {"name": "Fred", "age": 17}
for key in my_dict:
    print(f"The keys are: {key}")
print("\n")

for key in my_dict.keys():
    print(f"The keys are: {key}")
print("\n")

for value in my_dict.values():
    print(f"The values are: {value}")
print("\n")

for key, value in my_dict.items():
    print(f"The key is: {key}, and the value is: {value}")
