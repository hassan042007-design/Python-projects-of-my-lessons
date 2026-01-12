# practical-slice-Email----------------------------------------------------------------------------------------------


email = "Hassan_Elhady@email.com"
print(email[0])
print(email[0:6])

print(email.index("@"))
print(email[0:email.index("@")]) # will print to sign @

print("=" *50)

# extract info from email

theName = input('what\'s yuor name ') .strip() .capitalize()
theEmail = input('what\'s yuor Email ') .strip()
userName = (theEmail[0:theEmail.index("@")]).strip() .capitalize()
theWeb = (theEmail[theEmail.index("@")+1:])

print(f"Hello {theName} \nyour Email is : {theEmail}" )
print(f"Your User name is : {userName} \nand Your website is {theWeb}  " )

