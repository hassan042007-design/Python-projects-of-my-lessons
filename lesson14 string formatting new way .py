# string formatting new way-------------------------------------------------------------------------------
# in new way just use {}  and .format(variable)
# {:s} = string
# {:d} = decimal
# {:f} = float
# to control Floating point {.numf}
# to control string {.nums}
# format money : {:,d} after three num will write ,
# Rearrange Items : when you have list if you want rearrange items make index arrange first tem = 0 

Name = "Hassan"
Age = 18
rank = 10.15

print("my name is:{}" .format("Hassan"))
print("my name is:{}" .format(Name))
print("my name is:{} and my age is:{}"  .format(Name, Age))
print("my name is:{:s} and my age is:{:d} and my rank is:{:f}" .format(Name, Age, rank))
print("my name is:{:s} and my age is:{:d} and my rank is:{:.2f}" .format(Name, Age, rank))

# {:s} = string
# {:d} = decimal
# {:f} = float

n = "Hassan"
l = "python"
y = 10 

print("My Name is:{:s} Iam {:s} Developer With {:d} Years Exprince "  .format(n, l, y))

# control floating point
num = 20
print("my number is:{:d}" .format (num))
print("my number is{:f}" .format (num))
print("my number is:{:.1f}" .format (num))
print("my number is:{:.2f}" .format (num))

# control string
t = "Hassan abdelfattah"
print("my name is {:s}" .format(t))
print("my name is {:.6s}" .format(t))

#format money
mymoney = 895412733649
print("my money in the Bank {:d}" .format(mymoney))
print("my money in the Bank {:_d}" .format(mymoney))
print("my money in the Bank {:,d}" .format(mymoney))

#Rearrange Items

a, b, c = "one", "two", "three"
print("hello {} {} {}" .format(a, b, c,)) # hello one two three
print("hello {0} {2} {1}" .format(a, b, c,)) # hello one three two
print("hello {1} {2} {0}" .format(a, b, c,)) # hello two three one

x, y, z = 10, 20, 30 
print("dimentions {} {} {}" .format(x, y, z))
print("dimentions {1:d} {2:d} {0:d}" .format(x, y, z))
print("dimentions {1:d} {2:d} {0:d}" .format(x, y, z))
print("dimentions {1:.1f} {2:.1f} {0:.1f}" .format(x, y, z))

# format in version 3.6 +

myName ="hassan"
myAge = "18"

print("MyName is : {myName} and my age is : {myAge}") #put
print(f"MyName is : {myName} and my age is {myAge}") 

