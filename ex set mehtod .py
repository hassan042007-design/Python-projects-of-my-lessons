p = {"Hash", "qout", "name"}
f = p.copy()
p.clear()
print(p)
print(f)

y = {"slash", "space", "exit", "name"}
c = f.union(y)
print(c) 

y.add(5)
print(y)

y.remove(5)
print(y)

y.discard("kkk")
print(y)

print(y.pop())

y.update(f)
f.update(y)
print(y)
print(f)
