# Break-pass-and-continue-------------------------------------------------------------------------
# continue : Skip The Element and Continue to Others 
# Break    : Stop at Spesific Element
# pass     : Skip Condition Uses for Makeing Cod True 





myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]


# continue

for num in myNumbers :

    if num == 13 :  # make skip for 13

        continue
    
    print(num)

print("*"*50)

# Break 

for num in myNumbers :

    if num == 13 :  # stop at elemnt 13

        break
    
    print(num)


print("*"*50)

for num in myNumbers :

    print(num)

    if num == 13 :  # stop after elemnt 13

        break
    

print("*"*50)

# pass

for num in myNumbers :

    if num == 13 :  # skip condition and keep going

        pass
    
    print(num)

