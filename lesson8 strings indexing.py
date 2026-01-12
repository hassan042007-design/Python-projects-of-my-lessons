# strings indexing & slicing-----------------------------------------------------------------------------------------
# [1] All data in python is object
# [2] Object Contain Elements
# [3] Every Element Has Index 
# [4] Python Use Zero Based Indexing (Index Start From Zero)
# [5] Use Square Brakets To Access Element ([])
# [6] Enable to Accessing Part Of string, Tubles or Lists 
# [7] Indexing Accessing One Element But Slicing Accessing Multible Elments 

mysting = "I Love python"
print(mysting[0]) # I
print(mysting[9]) # t
print(mysting[-1]) # n (From End)
print(mysting[-6]) # P (From End)

# sliceing 
# [Start:End]
# [Start:End:Steps]
print(mysting[8:11]) # yth
print(mysting[3:5]) # ov

print(mysting[:10]) # Start From Zero (I love pyt)
print(mysting[5:]) # will go to end (e Python)
print(mysting[:]) # full data

print(mysting[0::1]) # I love Python 
print(mysting[0::2]) # Take Character and avoid Character
print(mysting[0::3]) # Take Character and avoid two Characters 




