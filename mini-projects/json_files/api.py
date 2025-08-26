import requests
import json

url = "https://randomuser.me/api/?results=5"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("API Data Retrieved Successfully:")
    print(json.dumps(data, indent=4))

    users = []
    for user in data['results']:
        users.append({
            "Name": f"{user['name']['first']} {user['name']['last']}",
            "Birth": user['dob']['date'],
            "Age": user['dob']['age'],
            "Gender": user['gender'],
            "Email": user['email'],
            "Location": f"{user['location']['city']}, {user['location']['country']}",
            "Phone": user['phone']
        })
    print("\nProcessed User Data:")

    with open("user.json", "w") as f:
        json.dump(users, f, indent=4)

    print("\nUser Data Saved Successfully!")

else:
    print("\nFailed to Retrieve API Data")