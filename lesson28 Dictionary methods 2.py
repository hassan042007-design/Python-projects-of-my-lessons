# Dictionary-methods-2-------------------------------------------------------------------------------
# setdefault(key , vlaue) : If key is Not Exisiting Will Add New Key And Value
# popitem() : print last item (key : value) in Dict  
# dict.item() : keep all changes in this variable
# dict.formkeys(var1 , var2) : make dict form two variables as (Keys , variables)

user = {
    "name" : "Hassan"
}
print(user)
print(user.setdefault("name" , "Ahmed"))
print(user)
print(user.setdefault("age" , "18"))
print(user)

print("=" *40)


member = {
    "name" : "Hassan",
    "long" : "177cm"

}

member.update({"age" : 18})
print(member)
print(member.popitem())

print("=" *40 )

view = {
    "name" : "Hassan",
    "skills" : "ps4"
}

allitems = view.items()
view.update({"age" : 18})
print(allitems)

print("=" *40)


# dict.formkeys()

a = ("mykeyOne", "mykeyThree", "mykeyTwo")
b = ("x")
print(dict.fromkeys(a, b))