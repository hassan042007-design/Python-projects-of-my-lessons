# strings formatting---------------------------------------------------------------------------------------
# %s : place holder can add string with num 
# %s = String 
# %d = Decimal
# %f = Float 
# to control Floating point %.numf
# to control string %.nums


Name = "Hassan"
Age = 18
rank = 10.15
print(("my name is:" +Name))
# print(("my name is:" + Name) + " and my age is:" + Age ) error can't add str with num

print("my name is:%s" % "Hassan")
print("my name is:%s" % Name)
print("my name is:%s and my age is:%d" %  (Name, Age))
print("my name is:%s and my age is:%d and my rank is:%f" %  (Name, Age, rank))

n = "Hassan"
l = "python"
y = 10 

print("My Name is:%s Iam %s Developer With %d Years Exprince " % (n, l, y))

# control floating point
num = 20
print("my number is:%d" % (num))
print("my number is:%f" % (num))
print("my number is:%.1f" % (num))
print("my number is:%.2f" % (num))

# control string
t = "Hassan abdelfattah"
print("my name is %.6s" % (t))