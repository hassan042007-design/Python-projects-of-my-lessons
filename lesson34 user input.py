# user-input--------------------------------------------------------------------------------------------


fName = input('Whats\' is your first name ')
mName = input('What\' is your middel name ')
lName = input('What\' is your last name ')

fName = fName.capitalize()
mName = mName.capitalize()
lName = lName.capitalize()

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()
print(f"Hello {fName} {mName:.1s} {lName} Happy to see you")