#Function Parametrs + Argument-------------------------------------------------------------------------

print([1])

# def           => Function Keyword [define]
# say_Hello()   => Function name
# name          =>parameter

def say_Hello(name):
    print(f"Hello {name}") # Have One Argument name

say_Hello("Hassan")    


a, b, c = "Ahmed", "Osama", "Sayed"

say_Hello(a)    
say_Hello(b)    
say_Hello(c)    


print("*"*50)
print([2])


def addition(n1 , n2) :

    print(n1 + n2) # Have Two Argument n1 , n2

addition(5, 10)
addition(-50, 100)

print("*"*50)
print([3])

# Use if condition to check n1 and n2 is numbers

def addition_2(n1 , n2) :

    if type(n1) != int or type(n2) != int:
        print("Only Integers Allowed")

    else :
        print(n1 + n2)

addition_2("100", 2)
addition_2(100, 2)

print("*"*50)
print([4])

# Full name 

def Fullname(first, middle, last) :
    
    print(
  f"Hello {first.strip().capitalize()} {middle.upper():.1} {last.strip().capitalize()}")
    
Fullname("Hassan","Abdelfattah","ElRussy" )

