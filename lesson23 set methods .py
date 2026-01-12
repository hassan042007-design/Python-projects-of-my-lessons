# Set Methods------------------------------------------------------------------------------------------------
# Clear  : Remove all Items in Set
# union  : Add Two sets by (|) or (.union)  
# add    : Add Item to Set
# copy   : take copy from set 
# remove : Remove  Designated Item
# discard: Diffrend From remove If Item is Not existing will not give error
# pop    : Give Random Element From Set
# update : like union but it don't rpeat the same itemes and can take items from list



# clear
a = {"U", "I", "J"}
a.clear()
print(a)


# union
b = {"One", "Two", "Three"}
c = {1, 2, 3}

print(b | c)
print(b.union(c))

# add
d = {1, 2, 3, 4}
d.add(5)
d.add(6)
d.add(7)
print(d)

# copy
e = {1, 2, 3, 4}
f = e.copy()

e.add("copy")
print(e)
print(f)

# remove
g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7) error
print(g)

# discard
q = {1, 2, 3, 4}
q.discard(7)
print(q)

# pop
i =  {"A", "C", True, 100.5}
print(i.pop())

# update()
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(k)
print(j)

k.update(j)
print(k)

l = ["html", "css", "java script"]
j.update(l)
print(j)