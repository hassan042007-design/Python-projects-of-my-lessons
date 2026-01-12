# List Method---------------------------------------------------------------------------------------------------------
# List.append("word") : add new word in list and add another list as one element
# List.extend(List-2) : defrrind from append add new list as apart of the majour list
# List.remove("word") : remove the designated word from list just once
# List.sort()         : arrange numbers of the list   (just all num or str)
# List.sort()         : arrange numbers of the list   (just all num or str)
# List.sort()         : arrange numbers of the list in reverse order (just all num or str)
# List.reverse()      : arrange list in reverse order not on the basis of A certain thing
  




# append()
myfrinds = ["Osama", "Hazem", "Ahmed"]
myoldfrinds =["ziad", "zaid", "marawan"]

myfrinds.append("Shrif")
myfrinds.append(100)
myfrinds.append(150.200)
myfrinds.append(False)
myfrinds.append(myoldfrinds)

print(myfrinds)
print(myfrinds[2]) # Ahmed 
print(myfrinds[-1]) # myoldfrinds list
print(myfrinds[7]) # myoldfrinds list 
print(myfrinds[7][2]) # myoldfrinds list specifies elment nubmer two

#extend()
a = ["A", "B", "C"]
b = [1, 2, 3]
c = ["one", "two"]

a.extend(b) 
a.extend(c)
print(a)


# remove()
x = ["A", "B", "C", "Hassan", 1, 2, 3, "one", "Hassan"]

x.remove("Hassan")
print(x)

# sort()
y = [1, 2, 100, 120, -10, 17, 29 ]
p = y.sort()
print(p)

o = y.sort(reverse=False) # Don't Arrange them in reverse order 
print(o)

u = y.sort(reverse=True) # Arrange them in reverse order 
print(u)

# reverse
z = [10, 1, 9, 80, 100, "Hassan", 100]
l = z.reverse()
print(l)

h = ["hassan" ,"ziad", "asmaa"]
d = h.sort()
print(d)