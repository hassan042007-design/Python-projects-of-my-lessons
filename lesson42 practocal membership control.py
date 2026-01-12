# Practical-Membership-Control-----------------------------------------------------------------------------------



# List contains Admins
admins = ["Ahmed", "Hussin", "Shakeir", "Hassan", "Mohamed", "Omar"]

# Login 
name = input("Please Type Your Name ").strip().capitalize()

# If Name Is in Admins :
if name in admins :
    print(f"Hello {name} Welcome Back")

    option = input("Delete Or Update Your Name ").strip().capitalize()

    #Update option

    if option == "Update" or option == "Up" :

        NewName = input("Type Your New Name ").strip().capitalize()

        admins[admins.index(name)] = NewName
        print("Name Updated.")

    # Delete option

    elif option == "Delete" or option == "Del" :
        admins.remove(name)
        print("Name Deleted")

    # Wrong Option

    else :
        print("Wrong Option Choosed")

# Not Admin  
else :
    status = input("You Are Not Admin , add you Y , N ").strip().capitalize()

    if status == "Y" or status == "Yes" :
        user = input("Type Your name ").strip().capitalize()
        if user in admins :
            print("You Are Admin Already")
        else:
            admins.append(user)
            print(f"Hello {user} You are Admin now")
            print(admins)

    elif status == "N" or status == "No" :
        print("As You Like Nice to Meet You")

    else :
        print("Wrong Option Choosed")