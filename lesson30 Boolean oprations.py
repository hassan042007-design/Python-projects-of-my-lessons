# Boolean oprations----------------------------------------------------------------------------------------
# and : must all conditions are valid to Give True
# or : must any conditions are valid to Give True


age =18
country = "Egypt"
print(age>15)
print(country == "Egypt")
rank = 10

#and
print(age>15 and country == "Egypt" and rank > 0) # True
print(age>15 and country == "KSA" and rank > 0) # False
print(age>15 and country == "Egypt" and rank == 0) # False

# or
print(age>15 or country == "Egypt" or rank > 0) # True
print(age>15 or country == "KSA" or rank > 0) # True
print(age>40 or country == "KSA" or rank > 20) # False
print(age>40 or country == "Egypt" or rank > 20) # True

# Not 
print(age > 16) # True
print(not age > 16) # Not True = False