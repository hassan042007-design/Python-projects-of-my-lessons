#count-age-detailse-------------------------------------------------------------------------------------

# write a Very Beautiful Note
print("*" * 80)
print(" You Can Write The First Letter or Full Name of The time Unit " .center(80))
print("*" * 80)

# collect age data
age = int(input("Please write Your age ").strip())

# collect time Unit Data 
unit = input("Please choose time Unit : Months , weaks , days ").strip().lower()

# Get time units
months = int(age) *12
weaks = int(months) *4
days = int(age) *365


if unit == "months" or unit == "m" or unit == "mo" or unit == "mon" :

    print("You choose the unit Months")
    print(f"You Lived {months :,} Months") 

elif unit == "weaks" or unit == "w" or unit == "we" or unit == "wea" :

    print("You choose the unit Weaks")
    print(f"You Lived {weaks :,} Weaks") 

elif unit == "days" or unit == "d" "days" or unit == "da" "days" or unit == "day" :
    print("You choose the unit Days")
    print(f"You Lived {days :,} Days") 

