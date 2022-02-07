import time

command1 = input("Enter command: ")
if command1 == "register":
	name1 = input("Name: ")
	password1 = input("Password: ")
	email1 = input("Email: ")
	time.sleep(1)
	print("loading...")
	time.sleep(1)
	print("Registered")
	print("User Data: ")
	print("Name: " + name1)
	print("Password: " + password1)
	print("Email: " + email1)
	print()
