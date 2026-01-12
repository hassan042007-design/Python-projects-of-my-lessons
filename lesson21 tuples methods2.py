# Tuples-method-2------------------------------------------------------------------------------------------------
# Tuple Treat With One Element As (str or int ...) you must add , After element 
# You Can Add Two Tuples as a concatenation
# Tuple, List, String Can Repeat(*)
# Tuple.count(item) : count repetition designated item 
# Tuple.index(item) : specify index of designated item
# Tuple Can Distribute to some items like (x, y, z) = Tuple This called Destrepution 



myTuple = ("Hassan")
myTuple1 = "Hassan"

print(type(myTuple)) # str
print(type(myTuple1)) # str

myTuple2 = 18
print(type(myTuple2)) # int

myTuple3 = ("Hassan",)
myTuple4 = (18,)
print(type(myTuple3)) # Tuple
print(type(myTuple4)) # Tuple

print(len(myTuple3))
print(len(myTuple4))

# concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B") + b

print((c))
print((d))

# Tuple, List, String Can Repeat(*)
myString = "Hassan"
myList = [1, 2]
myTuple5 = ("A", "B")

print(myString*6)
print(myList*6)
print(myTuple5*6) 

n = (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(n.count(1))

b = (1, 3, 7, 11)
print(b.index(7))

# print("The Position of Index is :" + b.index(7)) Error
print("The Position of Index is : {:d} " .format( b.index(7)))
print(f"The Position of Index is : {b.index(7)}") # Mex Tuple and Str formating


# Tuple Destruct
g = ("A", "B", "C")

x, y, z = "A", "B", "C"
print(x)
print(y)
print(z)

x, y, z = g
print(x)
print(y)
print(z)

f = ("A", "B", 4, "C")
x, y, _, z = f
print(x)
print(y)
print(z)