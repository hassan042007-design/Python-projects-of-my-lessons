# Membership-Operator--------------------------------------------------------------------------------------------------------------
# in : Do the object Is Existing in the variable
# not in : Do the object Is not Existing in the variable
# You Can Use in and not in With condition




# string
name = "Hassan"
print("s" in name)
print("a" in name)
print("H" in name)

print("=" *50)

# List 
friends = ["Ahmed", "Hussin", "Shakeir"]
print("Hussin" in friends) # True
print("Mohamed" in friends) # False
print("Mohamed" not in friends) # True
print("Shakeir" not in friends) # Fasle

print("=" *50)
 
# Use in and not in With condition
counties1 = ["Egypt", "KSA", "Kuwait", "Bahrain"]
counties1Discount = 80

counties2 = ["Italy", "USA"]
counties2Discount = 50

mycountry = "Egypt"

if mycountry in counties1 :
    print(f"Hello You Have a Discount Equal To ${counties1Discount}")

elif mycountry in counties2 :
    print(f"Hello You Have a Discount Equal To ${counties2Discount}")

else:
    print("You Don't Have any Discount")
     