i = ["error", "in no vain", "in no vain"]
g = i.copy()
i.clear()
print(i)
print(g)

print(g.count("in no vain"))

print(g.index("error"))
print(g.pop(0))

o = ["error", "in no vain", "in no vain"]
o.insert(1, "nothing")
print(o)