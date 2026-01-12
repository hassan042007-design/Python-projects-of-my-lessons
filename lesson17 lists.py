# lists -------------------------------------------------------------------------------------------------------
# List Items Are Enclosed in Square Brackets
# List Are Ordered, To Use Index To Access Item
# List Are Mutable => Add, Delete, Edit
# List Items is Not Unique
# List Can Have Different Data Types 
    

MyAwesomeList = ["one", "two", "one", 1, 100.5, True ]
print(MyAwesomeList) # whole list 
print(MyAwesomeList[0]) # one 
print(MyAwesomeList[2]) # one
print(MyAwesomeList[4]) # 100.5
print(MyAwesomeList[-1]) # true
print(MyAwesomeList[-3]) # 1

# Slice List 
print(MyAwesomeList[1:4]) # [two, one, 1]
print(MyAwesomeList[:4]) 
print(MyAwesomeList[1:]) 

print(MyAwesomeList[::1]) # Step By Step
print(MyAwesomeList[::2]) # Step And Skip Step
print(MyAwesomeList[::3]) # Step And Skip Two Steps

MyAwesomeList[1] = 2 
print(MyAwesomeList) # reblace the designated index to another object

print(MyAwesomeList) 

MyAwesomeList[0:3] = ["A", "B", "C"]
print(MyAwesomeList) 

MyAwesomeList[0:3] = ["A"]
print(MyAwesomeList) # Replace All Slice To Just "A"


