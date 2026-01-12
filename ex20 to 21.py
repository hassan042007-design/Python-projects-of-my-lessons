# Ex Tuple

name = "Hassan",
print(name)
print(type(name))

frinds = ("Osama", "Omar", "Zaid")
frinds_list = list(frinds)
frinds_list[0] = "Elzero"

frinds = tuple(frinds_list)
print(frinds)
print(type(frinds))
print(len(frinds))


num = (1, 2, 3)
words = ("A", "B", "C")
c = num + words
print(c)
print(len(c))

tuple = (1, 2, 3)
x, y, z = tuple
print(x)
print(y)
print(z)
