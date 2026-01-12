# Dictionary-Methods---------------------------------------------------------------------------------
# clear : remove all Items
# Dict[key] = Value : add new Key and Value
# update({key : value}) : add new Key and Value
# copy : take copy from main Dict



#clear
user = {
    "name" : "Hassan"
}
print(user)
user.clear()
print(user)

print("=" *40) 


# Dict[key] = Value : add new Key and Value

member = {
    "name" : "Hassan"
}

print(member)
member["age"] = 18
print(member)

# update({key : value}) : add new Key and Value
member.update({"ranke" : "10.5"})
print(member)

print("=" *40) 


# copy()
main = {
    "name" : "Hassan"
}

R = main.copy()
main["age"] = "18"
main.update({"long" : "177cm"})
print(main)
print(R)