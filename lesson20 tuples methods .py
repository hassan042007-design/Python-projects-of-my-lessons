# Tuples-methods-------------------------------------------------------------------------------------------------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses
# [3] Tuple Are Ordared, To Use Index To Access Item
# [4] Tuple Are Immuteble = You Can't Add or Delet 
# [5] Tuple Item Is Not Unique 
# [6] Tuple Can Have Defferent Data Types
 

myTuple = ("Hassan", "Ahmed")
myTuple2 = "Hassan", "Ahmed"

print(myTuple)
print(myTuple2)


print(type(myTuple))
print(type(myTuple2))

myTuple3 = (1, 2, 3, 4, 5)
print(myTuple3[2])
print(myTuple3[-2])

myTuple4 = ("Hassan", "Hassan", 1, 2, 3, 100.5, True )
print(myTuple4)
print(myTuple4[1])

print(myTuple4[-1])