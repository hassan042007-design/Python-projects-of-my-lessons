# string-methods-3 -----------------------------------------------------------------------------------------
# index(Subsrtring, Start, End) : num of character in syntax if can't find will give error 
# find() : deffrint about index if character not found will give (-1)
# rjust(width, "fill char") , ljust(width, "fill char") : make space or char before or after syntax 
# splitlines : make lines of string in the list
# expandtabs(num) : increase tap behynd \t
# is"type"() : do this variable is pla
# the deffrint betwin isdecimal and isalnum : isdecimal can't have any thing but num isalnum can have any thing character or num
# isidentifier : do this syntax be variable 


a = "I love Python"
print(a.index("P"))
print(a.index("P", 0, 10))
#print(a.index("P", 0, 5)) # error not founded

b = "I love Python"
print(b.find("P"))
print(b.find("s"))


c = "Hassan"
print(c.rjust(10))
print(c.rjust(10, "#"))
print(c.ljust(10))
print(c.ljust(10, "#"))


f = """ hassan
abdelfattah
hassan """
print(f.splitlines())
print(type( f.splitlines()))

e = "first \nsecond \nthird line"
print(e)
print(e.splitlines())

l = "Hello\tfrind\tI\tlove\tPython"
print(l)
print(l.expandtabs(20))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle()) # true
print(two.istitle()) # false
print(one.islower()) # false

three = " "
print(three.isspace()) # true

four = "01033154682" 
print(four.isdecimal()) # true

five = "hassan123"
print(five.isalnum()) # true 


six = "hassan100"
seven = "hassan--100"
print(six.isidentifier()) # true
print(seven.isidentifier()) # false

x = "AAaaaBa"
y = "AAaaaBa123"
print(x.isalpha()) # true
print(y.isalpha()) # false 
print(x.isalnum()) # true
print(y.isalnum()) # true