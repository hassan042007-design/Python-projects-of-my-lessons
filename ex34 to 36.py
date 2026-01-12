name = input('what\'s your name ')
name = name.capitalize().strip()
print(f"Hello {name} Welcome in our website ")


age = int(input("inter your age "))

if age < 16:
    print("this art not suitable for you")

if age > 16: 
    print("welcom your age is suitable for our arts")



first_name = input("Enter your first name ")
second_name = input("Enter your second name ")

first_name = first_name.strip().capitalize()
second_name = second_name.strip().capitalize()

print(f"hello {first_name} {second_name:.1s} in")


email = input("inter your email ")
email = email.lower().strip()

print("your name is" , email[0:email.index("@")].capitalize())
print("Email Service Provider Is",email[email.index("@")+1:email.index(".")])
print("Top Level Domain", email[email.index(".") : ])

