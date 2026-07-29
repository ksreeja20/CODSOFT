contacts=[]

while True:
    print("\n===== CONTACT BOOK =====")
    print("1.Add Contact\n2.View Contacts\n3.Search Contact\n4.Update Contact\n5.Delete Contact\n6.Mark Emergency Contact\n7.Total Contacts\n8.Exit")
    ch=input("Enter your choice: ")

    if ch=="1":
        name=input("Enter Name: ")
        phone=input("Enter Phone: ")
        if any(c["Phone"]==phone for c in contacts):
            print("Contact already exists!")
        else:
            contacts.append({"Name":name,"Phone":phone,"Emergency":False})
            print("Contact Added Successfully!")

    elif ch=="2":
        if not contacts:
            print("No contacts found.")
        else:
            for c in contacts:
                if c["Emergency"]:
                    print("🚨 EMERGENCY CONTACT")
                print("Name :",c["Name"])
                print("Phone:",c["Phone"])
                print("-"*20)

    elif ch=="3":
        key=input("Enter Name or Phone: ")
        found=False
        for c in contacts:
            if c["Name"].lower()==key.lower() or c["Phone"]==key:
                if c["Emergency"]:
                    print("🚨 EMERGENCY CONTACT")
                print("Name :",c["Name"])
                print("Phone:",c["Phone"])
                found=True
                break
        if not found:
            print("Contact not found.")

    elif ch=="4":
        phone=input("Enter Phone to Update: ")
        for c in contacts:
            if c["Phone"]==phone:
                c["Name"]=input("New Name: ")
                c["Phone"]=input("New Phone: ")
                print("Updated Successfully!")
                break
        else:
            print("Contact not found.")

    elif ch=="5":
        phone=input("Enter Phone to Delete: ")
        for c in contacts:
            if c["Phone"]==phone:
                contacts.remove(c)
                print("Deleted Successfully!")
                break
        else:
            print("Contact not found.")

    elif ch=="6":
        phone=input("Enter Phone: ")
        for c in contacts:
            if c["Phone"]==phone:
                c["Emergency"]=True
                print("Marked as Emergency Contact!")
                break
        else:
            print("Contact not found.")

    elif ch=="7":
        print("Total Contacts:",len(contacts))

    elif ch=="8":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
