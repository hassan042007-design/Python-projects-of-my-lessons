h = "hassan abdelfattah"
print(h.index("h"))
print(h.find("h"))
print(h.count("h"))
print(len(h))
print(h.find("c")) # -1



print(h.rjust(30, "("))
print(h.ljust(30, ")"))
print(h.center(30, ")"))

p = ''' BMW 
is 
my 
dream 
car '''
print(p.splitlines())

g = "BMW\tis\tmy\tdream\tcar"
print(g.expandtabs(10))

one = " "
print(one.isspace())

two = "nononono097"
print(two.isalnum())
print(two.isalpha())

three = "python--language"
print(three.isidentifier())

# replace()
k = "I Love Mercedes"
print(k.replace("Mercedes", "BMW"))

# .join()
u = ["BmW", "Mercedes", "skoda", "icecream"]
print(" ".join(u))
print(" - ".join(u))
