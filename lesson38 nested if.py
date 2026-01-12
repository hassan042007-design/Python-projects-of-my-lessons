# Nested-If-------------------------------------------------------------------------------------------------------
# or : make condition applied on more than resone



uName = "Hassan"
isstudent = "Yes"
uCountry = "Egypt"
cName = "python course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":


    if isstudent == "Yes" : 
         print(f"Hello {uName} Because you are from {uCountry} and stydent")
         print(f"the course \"{cName}\" price is ${cPrice - 90}") 

    else : 
        print(f"Hello {uName} Because you are from {uCountry}")
        print(f"the course \"{cName}\" price is ${cPrice - 80}") 

elif uCountry == "Kuwait" or uCountry == "Bahrain":

    print(f"Hello {uName} Because you are from {uCountry}")
    print(f"the course \"{cName}\" price is ${cPrice - 50}")

else:  

    print(f"Hello {uName} Because you are from {uCountry}")
    print(f"the course \"{cName}\" price is ${cPrice - 30}") 

