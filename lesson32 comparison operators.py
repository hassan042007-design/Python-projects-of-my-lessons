# Comparison-Oprators------------------------------------------------------------------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than OR Equal
# [ <= ] Less Than OR Equal


# Equal + Not Equal 

print(100 == 100) # True
print(100 == 200) # False
print(100 == 100.00) # True

print("=" * 50)

print(100 != 100) # False
print(100 != 200) # True
print(100 != 100.00) # False

print("=" * 50)

# Greater Than + Less Than

print(100 > 100) # False
print(100 > 200) # False
print(100 > 100.00) # False
print(100 > 40) # True

print("=" * 50)

print(100 < 100) # False
print(100 < 200) # True
print(100 < 100.00) # False
print(100 < 40) # False

print("=" *50)

print(100 >= 100) # True
print(100 >= 200) # False
print(100 >= 100.00) # True
print(100 >= 40) # True

print("=" *50)

print(100 <= 100) # True
print(100 <= 200) # True
print(100 <= 100.00) # True
print(100 <= 40) # False