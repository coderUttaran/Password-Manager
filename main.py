store = {}

def add_password():
    global store
    user_web = input("Enter Website: ")
    user__password = input("Enter Password for it: ")
    print()
    if user_web not in store.keys():
        store[user_web] = user__password
        print("Stored Successfully")
    else:
        print("Your are updating it....")
        store[user_web] = user__password
        print("Updated Successfully")

def delete_web():
    global store

    user_web = input("Enter Website to delete: ")
    print()
    if user_web not in store.keys():
        print("Website not in our database")
    else:
        del store[user_web]
        print("Deleted Successfully")

def search_password():
    global store

    user_web = input("Enter the website to search for password: ")
    print()
    if user_web not in store.keys():
        print("This website is not in our database")
    else:
        print(f"The password for {user_web} is:")
        print(store[user_web])

def show_passwords():
    for values in store:
        print(f"{values} : {store[values]}")


def main():
    print("----Welcome Password manager----\n")
    
    while True:

        print("Choose operation: ")
        print("""1 - Add Password
2 - Delete Website
3 - Show Passwords
4 - Search for password""")
        print()
        choice = input("Enter operation no. : ")
        print()

        if choice == "1":
            add_password()
        elif choice == "2":
            delete_web()
        elif choice == "3":
            show_passwords()
        elif choice == "4":
            search_password()
        else:
            print("Invalid choice")
        print()
        cont = input("Would you like to continue? [Y/n]: ")
        if cont != "Y":
            print("Thank you for using Password Manager")
            print("Closing password manager.....")
            break
main()
