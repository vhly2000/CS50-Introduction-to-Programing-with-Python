#Ask user for their name
name = input("What's your name? ").strip().title()

#split user's name into first and last name 
first, last = name.split(" ")

#Say hello to user with their name
print(f"Hello, {first}")

