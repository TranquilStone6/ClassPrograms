friends_dict = {}

def menu():
    while True:
        print("\nMENU:")
        print("1. Create/Add a Dictionary in the form {Name: PhoneNumber}")
        print("2. Display name and phone number of all friends")
        print("3. Add new key:value pair and display modified dictionary")
        print("4. Delete a particular entry from dictionary")
        print("5. Check if a name is present in the dictionary")
        print("6. Modify a particular value")
        print("7. Display the dictionary in sorted order of names")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            num_entries = int(input("Enter the number of friends to add: "))
            for _ in range(num_entries):
                name = input("Enter friend's name: ")
                phone_number = input("Enter phone number: ")
                friends_dict[name] = phone_number
            print("Dictionary created/updated.")

        elif choice == '2':
            if not friends_dict:
                print("No data available.")
            else:
                print("\nFriend's Name and Phone Numbers:")
                for name, phone_number in friends_dict.items():
                    print(f"{name}: {phone_number}")

        elif choice == '3':
            name = input("Enter friend's name to add: ")
            phone_number = input("Enter phone number: ")
            friends_dict[name] = phone_number
            print("New entry added successfully.")
            print(friends_dict)

        elif choice == '4':
            name_to_delete = input("Enter the name to delete: ")
            if name_to_delete in friends_dict:
                del friends_dict[name_to_delete]
                print(f"Entry for {name_to_delete} deleted.")
            else:
                print(f"{name_to_delete} not found in the dictionary.")

        elif choice == '5':
            name_to_search = input("Enter the name to search: ")
            if name_to_search in friends_dict:
                print(f"{name_to_search} is present with phone number {friends_dict[name_to_search]}.")
            else:
                print(f"{name_to_search} not found in the dictionary.")

        elif choice == '6':
            name_to_modify = input("Enter the name whose phone number you want to modify: ")
            if name_to_modify in friends_dict:
                new_phone_number = input("Enter the new phone number: ")
                friends_dict[name_to_modify] = new_phone_number
                print(f"Phone number for {name_to_modify} has been updated.")
            else:
                print(f"{name_to_modify} not found in the dictionary.")

        elif choice == '7':
            if not friends_dict:
                print("No data available.")
            else:
                sorted_friends = dict(sorted(friends_dict.items()))
                print("\nDictionary sorted by names:")
                for name, phone_number in sorted_friends.items():
                    print(f"{name}: {phone_number}")

        elif choice == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option (1-8).")


menu()
