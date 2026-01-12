# string method-----------------------------------------------------------------------------
# len: count num of characters
# strip() : skip space of syntax 
# rstrip() : skip space of syntax from right
# lstrip() : skip space of syntax from lift
# title() : make syntax title first character and character after num capital  
# capitalize() : make just first character from first word  
# zfill(num) : write zero before character to make variables sam nums
# upper : write words with capital character
# lower : write words with smaller character


a = "I Love Python"
b = "    I Love Python       "
print(len(a))
print(len(b))
print(b.strip())
print(b.rstrip())
print(b.lstrip())



c = "@#@#@#I Love Python@#@#@#"
print(c.strip("@#"))
print(c.rstrip("@#"))
print(c.lstrip("@#"))

d = "i make 3d models and graghic dsign"
print(d.title())

print(d.capitalize())


P, D, F = "1", "11", "111"
print(P)
print(D)
print(F)

print(P.zfill(3))
print(D.zfill(3))
print(F.zfill(3))

name = "Hassan Abd elfattah"
print(name.upper())
print(name.lower())
print("hassan".upper())