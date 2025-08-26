import json

with open("data.json","r") as file:
    data = json.load(file)
    print("Original Data")
    print(data)
    
# If the top-level JSON object is a list, add/update the Status field on each item.
if isinstance(data, list):
    for item in data:
        if isinstance(item, dict):
            item["Status"] = "Processed"
else:
    # If it's a dict, set Status directly.
    if isinstance(data, dict):
        data["Status"] = "Processed"

with open("updated_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nUpdated Json Saved! -> updated_data.json")