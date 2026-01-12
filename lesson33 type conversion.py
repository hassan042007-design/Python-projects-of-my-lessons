# type-conversion------------------------------------------------------------------------------------------
# str()
# tuple() 
# list()
# set()
# dict() : will give error if there not key and value


# str
a = 10 
print(type(a))
print(type(str(a)))

print("=" *50)

# tuple()

c = "Hassan" # str
d = [1, 2, 3, 4, 5] # List
e = {"A", "B", "C"} # Set
f = {"A" : 1 , "B" : 2} # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

# print(tuple(500)) error

print("=" *50)

#list()

g = "Hassan" # str
h = (1, 2, 3, 4, 5) # Tuple
i = {"A", "B", "C"} # Set
j = {"A" : 1 , "B" : 2} # Dictionary

print(list(g))
print(list(h))
print(list(i))
print(list(j))  

print("=" *50)


# Set()

k = "Hassan" # str
l = (1, 2, 3, 4, 5) # Tuple
m = ["A", "B", "C"] # lsit
n = {"A" : 1 , "B" : 2} # Dictionary

print(set(k))
print(set(l))
print(set(m))
print(set(n)) 

print("=" *50)

# dictionaty()

# o = "Hassan" # str error
p = (("A",1), ("B", 2), ("C",3)) # Tuple
q = [["A",1], ["B" ,2], ["C" ,3]] # lsit
# r = {{"A" :1} ,{"B":2} } # set error un hasheble

# print(dict(o))
print(dict(p))  
print(dict(q))
# print(dict(r))