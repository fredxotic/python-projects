try:
    with open("python-lessons/Practice_File.txt") as file:
        content = file.read()
        print(content.upper())

except FileNotFoundError:
    print("File not found!")