# If-Else-Elif -------------------------------------------------------------------------------------------------------
#  if condition :
#  else : use when the if condition is not achieved
#  elif : use when you have more than one condition
# 


uName = "Hassan"
uCountry = "Kuwait"
cName = "python course"
cPrice = 100

if uCountry == "Egypt":

    print(f"Hello {uName} Because you are from {uCountry}")
    print(f"the course \"{cName}\" price is ${cPrice - 80}") 

elif uCountry == "KSA":

    print(f"Hello {uName} Because you are from {uCountry}")
    print(f"the course \"{cName}\" price is ${cPrice - 60}")

elif uCountry == "Kuwait":

    print(f"Hello {uName} Because you are from {uCountry}")
    print(f"the course \"{cName}\" price is ${cPrice - 50}")

else:  

    print(f"Hello {uName} Because you are from {uCountry}")
    print(f"the course \"{cName}\" price is ${cPrice - 30}") 

