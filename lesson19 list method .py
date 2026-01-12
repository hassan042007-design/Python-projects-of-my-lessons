#-List-method-2--------------------------------------------------------------------------------------------------
# List.clear()             : remove all items in the list 
# List.copy()              : take copy with keep the main version
# List.count(item)         : count repetition designated item 
# List.index(item)         : specify index of designated item
# list.insert(index , item): like append and extend but add new item befor  spesify index
# list.pop(index)          : extract item from it index




# clear()
a = [1, 2, 3, 4, 5]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

b.append(5)

print(b)
print(c) # the copy will keep the original list 

# count()

L = [1, 2, 3, 1, 2, 3, 1 ]
print(L.count(1))

# index

N = ["Liam","Noah","Oliver","Theodore","James","Henry","Mateo","Elijah","Lucas","William","Benjamin","Levi","Ezra","Sebastian","Jack"]
print(N.index("Jack"))


# insert()
o = [1, 2, 3, 4]
o.insert(0, "Test")
print(o)

q = [1, 2, 3, 4]
q.insert(1, "Test")
print(q)



t = [1, 2, 3, 4]
t.insert(-1, "Test")
print(t)

# pop()
f = ["go", "went", "set", "b"]
print(f.pop(0))
print(f.pop(-1))
print(f.pop(1))

z = ["s", "w"]
print(z.pop(0))
print(z.pop(-1))

