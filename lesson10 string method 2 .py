# string method 2------------------------------------------------------------------------------------------------
# split() : part words of string in list
# max split() = split(,num) : num of time will split
# rsplit() : start from right
# center(num) : make syntax in the center sround by space
# center(num, %) : make syntax in the center sround by %
# count("word") : Count how many times word repeat in The syntax
# swapcase() : Make Capital Character Small and Small Character Capital
# startswith(Character x) : Do the syntax Starts with Character x
# endswith(Character x) : Do the syntax ends with Character x
a = "I Love Python and PHP"
print(a.split())


b = "I-Love-Python-and-PHP"
print(b.split("-"))

#max split

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-",2))
print(c.split("-",3))

print(c.split("-",2))
print(c.rsplit("-",3))

e = "Hassan"
print(e.center(9)) # spaces
print(e.center(10,"%")) # %
print(e.center(10,"#")) # Hashes

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))
print(f.count("Love"))
print(f.count("PHP", 0, 25))
print(f.count("PHP", 0, 35))


g = "I Love Python"
h = "i lOVE pYTHON"
print(g.swapcase())
print(h.swapcase())

i = "I Love Python"
print(i.startswith("I")) # True
print(i.startswith("S")) # False
print(i.startswith("P",7, 12)) #True

print(i.endswith("n")) # True
print(i.endswith("e")) # False
print(i.endswith("e",0, 6)) # true

