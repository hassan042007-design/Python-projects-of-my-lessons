#-string methods 4 -----------------------------------------------------------------------------------------
# replace(old value, new value, count)
# .join(Interable) : Transform list to string

a = "Mercedes is my dream car"
print(a.replace("Mercedes", "BMW"))

b = "Hello One Two One One three "
print(b.replace("One","1"))
print(b.replace("One","1", 2))

Myname =  ["Hassan", "Abdelfattah", "Hassan"]
print("".join(Myname))
print(" ".join(Myname))
print("-".join(Myname))
print(",".join(Myname))
print(type(",".join(Myname)))