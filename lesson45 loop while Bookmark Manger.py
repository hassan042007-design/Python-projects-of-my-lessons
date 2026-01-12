# loop while Bookmark Manger




# Empty List to Fill Later

MyFavouritewebs = []


# Maximum Allowed Website
maximumWebs = 5


while maximumWebs > 0 :
    web = input("Website Name Without https:// ").lower().strip()

    # Add The New Website To The List 
    MyFavouritewebs.append(f"https:// {web} ")
    maximumWebs -= 1

    if maximumWebs > 0 :
        print(f"You can add {maximumWebs}")

else :
    print(MyFavouritewebs)
    print("Book Mark is Full You can't add More")


# Check If list is Not Empty
if len(MyFavouritewebs) > 0 :

    # Sort The List 
    MyFavouritewebs.sort()

    index = 0

    print("printing The List Of Websites in BookMark")

    while index < len(MyFavouritewebs) :
        print(MyFavouritewebs[index])
        
        index += 1

        