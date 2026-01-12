a= "hassan abdelfattah hassan"
b= "hassan-abdelfattah-hassan"

print(a.split())
print(a.split(" ",1))
print(b.split("-"))
print(b.rsplit("-",1))

c = "Hassan"
print(c.center(16))
print(c.center(16,"^"))

p = "hI gAYS wASSAP"
print(p.swapcase())
print(p.startswith("h",3, 5))
print(p.endswith("P"))

k = "hello frind wassap frind bay frind"
print(k.count("frind"))