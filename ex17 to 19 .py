names = ["Hazem", "Samy", "salwa", "Nataly", "Pajero"]
print(names[0]) # Hazem
print(names[1]) # Samy
print(names[-5])# Hazem
print(names[-4]) # Samy

print(names[4]) # Pajero
print(names[-1]) # Pajero

print(names [::2]) # Even Names 
print(names [1::2]) # Odd Names

print(names [1:4]) # "Samy", "salwa", "Nataly"
print(names[3:5])

names.append("Saly")
print(names)

names.insert(0, "Jhony")
print(names)

names.remove("Jhony")
names.remove("Hazem")
names.remove("Saly")
print(names)

frinds = ["Hannen", "Maram"]
Arab = ["Ameen", "Ahmed"]
names.extend(frinds)
names.extend(Arab)
print(names)

names.sort()
print(names)
names.sort(reverse=True)
print(names)

print(len(names))

lang = ["Html", "CSS", "JS", "Python"]
fram = ["Django", "Flask", "Web"]
lang.append(fram)
print(lang)
print(lang[-1]  [0])
print(lang[-1]  [2])
