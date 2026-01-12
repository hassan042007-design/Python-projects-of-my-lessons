mypass = "123"

tries = 4 

inputpass = input("Write Your Password : ") 

while inputpass != mypass :

    tries -= 1

    print(f"Wrong Pass {"The Last" if tries == 0 else tries} Chance Left")
    inputpass = input("Rewrite The Password again : ").capitalize().strip()

    if tries == 0 :
            print("You Cant Try again")
            break
    
else :
      print("Welcom In Our Website")
        

