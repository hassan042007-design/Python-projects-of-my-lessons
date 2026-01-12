# Set-methods-2-----------------------------------------------------------------------------------
# difference()                 : Show Items which Mentioned in first set and didn't mentioned in second set
# difference_update()          : Keep The different Items in the Origonal set 
# intersection()               : Show The Similarity Between Two Sets
# intersection()_update        : Keep The Similarity Items in the Origonal set 
# symmetric_difference()       : Show Items never intersect  in Two sets
# symmetric_difference_update(): Keep Items never intersect in the Origonal set 



a = {1, 2, 3, 4}
b = {1, 2, "Osama", "Ahmed"}
print(a)
print(a.difference(b)) # a-b

print("=" *40) # Separator


# differece-update()
c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"} 
print(c)
c.difference_update(d)
print(c)

print("=" *40) # Separator


# intersection()

e = {1, 2, 3, 4, "x", "Osama"}
f = {"Osama", "x", 2}
print(e)
print(e.intersection(f))

print("=" *40) # Separator


# intersection_update()

e = {1, 2, 3, 4, "x", "Osama"}
f = {"Osama", "x", 2}
print(e)
e.intersection_update(f) # e & f
print(e)

print("=" *40) # Separator


# symmetric_diffrence()

i = {1, 2, 3, 4, 5, "x"}
j = {"Osama", "Zero", 1, 2, 4}
print(i)
print(i.symmetric_difference(j)) # i ^ j

print("=" *40) # Separator


# symmetric_diffrence()

k = {1, 2, 3, 4, 5, "x"}
l = {"Osama", "Zero", 1, 2, 4}
print(k)
k.symmetric_difference_update(l)
print(k)

