# Ternary-conditional-oprator----------------------------------------------------------------------------------------------


country = "Egypt"


if country == "Egypt" : print(f"The Weather in {country} Is 15c")

elif country == "KSA" : print(f"The Weather in {country} Is 30c")

else : print("country Is not In The List")


# Short if 

movierate = 18
age = 16

if age < movierate : # Condition If True

    print("Movie Is Not for You")

else :  #Condition If False

    print("Movie Is Good for You & Happy Watching")



# Condition If True | else | If condition False 
print("Movie Is Not for You" if age < movierate  else "Movie Is Good for You and Happy Watching")