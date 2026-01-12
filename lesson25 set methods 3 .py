# set method 3------------------------------------------------------------------------------------
# issuperset() : Do all Items in second set are existing in first set
# issubset()   : Do all Items in first set are existing in second set
# isdisjoint() : Do There any Item is Joint



# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b)) # True
print(a.issuperset(c)) # Fales

print("=" *40)


# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e)) # Fales
print(d.issubset(f)) # True
print(e.issubset(d)) # True

print("=" *40)


# isdisjoint

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}
print(g.isdisjoint(h)) # Fales
print(g.isdisjoint(i)) # True



