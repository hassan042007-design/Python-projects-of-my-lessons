names = ["Liam","Noah","Oliver","Theodore","James","Henry","Mateo","Elijah","Lucas","William","Benjamin","Levi","Ezra","Sebastian","Jack"]
names.sort()
print(names)

names.sort(reverse=True)
print(names)

firsttable = ["Liam","Noah","Oliver","Theodore","James","Henry","Mateo","Elijah","Lucas"]
secondtable = ["William","Benjamin","Levi","Ezra","Sebastian","Jack"]

firsttable.append(secondtable)
print(firsttable)

first = ["Liam","Noah","Oliver","Theodore","James","Henry","Mateo","Elijah","Lucas"]
second= ["William","Benjamin","Levi","Ezra","Sebastian","Jack"]

first.extend(second)
print(first)