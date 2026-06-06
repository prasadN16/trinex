def check_password(password):
    if len(password) >= 8:
        print("Strong Password")
    else:
        print("Weak Password")

while True:
    print("\n1. Check Password")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pwd = input("Enter Password: ")
        check_password(pwd)
    elif choice == "2":
        break