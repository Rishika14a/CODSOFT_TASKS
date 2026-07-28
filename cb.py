contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")

    elif choice == "2":
        if contacts:
            print("\nContact List")
            for name, details in contacts.items():
                print("------------------------")
                print("Name:", name)
                print("Phone:", details["Phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])
        else:
            print("No contacts found.")

    elif choice == "3":
        search = input("Enter contact name: ")

        if search in contacts:
            print("Name:", search)
            print("Phone:", contacts[search]["Phone"])
            print("Email:", contacts[search]["Email"])
            print("Address:", contacts[search]["Address"])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name in contacts:
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")

            contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")