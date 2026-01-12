num1 = int(input("Num1 = ").strip())
num2 = int(input("Num2 = ").strip())
operation = input("operation = \"+\" or \"-\" or \"*\" or \"/\" :  ") .strip()

if operation == "+" :
    print(num1 + num2)

if operation == "-" :
    print(num1 - num2)

if operation == "*" :
    print(num1 * num2)

if operation == "/" :
    print(num1 / num2)


age = 17 
print("app is suitable for you" if age> 16 else "app is not suitable for you" )


Uage = int(input("add your age "))

if Uage >10 and  Uage<100 :
    choose = input("choose age unit [day-weak-month-minute-second-hour]").strip().capitalize()
    if choose == "Day" :
            print(Uage *365)

    elif choose == "Month" :
            print(Uage *12)

    elif choose == "Weak" :
            print(Uage *12 *4)

    elif choose == "Hour"  :
            print(Uage *365 *24)

    elif choose == "Minute" or choose == "Min"  :
            print(Uage *365 *24 * 60)

    elif choose == "Second" or choose == "Sec" :
            print(Uage *365 *24 * 60 *60)

    else :
            print("Wrong choose")

else : 
    print("Out of Range")



