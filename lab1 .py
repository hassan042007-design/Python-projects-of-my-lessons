#----numpy----
# 

import numpy as np

a = np.array ([1, 0])
b = np.array ([2,6])

add = np.add(a, b)
sub = np.subtract(a, b)


print(add)
print(sub)

mult = np.multiply(a, b)
print(mult)


div = a/b 
print(div)

norm = np.linalg.norm(a)
print(norm) # sqaur root

c = 2*b

print(np.allclose(b,c))


d = np.array[0, 1]
print(np.b)