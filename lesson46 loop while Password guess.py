# while loop password guess---------------------------------------------------------------------




tries = 4

mainpass = "Hassan123"

inputpass = input("Write Your Password: ").capitalize().strip()

while inputpass != mainpass :

    tries -= 1

    print(f"Wrong password, {"The Last" if tries == 0 else tries} chacne Left")
    inputpass = input("reWrite Your Password again: ").capitalize().strip()

    if tries == 0 :

        print("You Can't Try again.")
        break 
        print("will not print")        

else :
    print("welcome in Our Website")

