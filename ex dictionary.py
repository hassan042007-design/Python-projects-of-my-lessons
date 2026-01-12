m = {
    "name " : "Yahia",
    "age" : 18,


}

print(m)
print(m.keys())
print(m.values())
print(m["age"])

frinds = {
    "wael" : { 
        "age" : 25, 
        "long" :180,
    },
    "Abanob" : {
        "age" : 23,
        "long" : 170
    }

}

print(frinds)
print(frinds["Abanob"])
print(frinds["Abanob"]["age"])
print(frinds["wael"]["long"])

print(len(frinds))
print(len(frinds["Abanob"]))

name = "hassan"
age = 18
skills = "bissnes man"
long = 177
IQ = 180

identify = {
    "first" : name,
    "second" : age,
    "third" : skills 
}
print(identify)

identify["fource"] = long
print(identify)

identify.update({"fifes" : IQ})
print(identify)

print(identify.setdefault("first", "h"))
print(identify.popitem())

see = identify.items()
print(see)

x = ("lenth",)
y = ("wide")
print(dict.fromkeys(x, y))