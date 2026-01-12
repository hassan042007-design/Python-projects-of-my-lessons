num = int(input("inter number "))

a = 0

# if num < 0 or num == 0 :

#         print("Add number more than 0")

# else:
#         while a < num :
    
#             if num == 6 :
#                 break
        
#             print(num-1-a)
#             a += 1 

                
                  

#         else : 
#                 print("The loop is done")

while a < num :
      
      c = num -1 -a


      a += 1

      if num == 0 or num < 0 :
            print("You must choose num more 0")  

      if c ==  6 or c == 0 :
            continue

      print(c)

else :
      print(f"The {num -2}  Numbers Printed Succesfully")



names = ["ahmed", "Shahd", "hassan", "Marawan", "Aldo" ]

o = 0 

p = []


while o < len(names) :
      
      if names[o].istitle() == True :
        print(names[o])


      if names[o].islower() == True :
           p.append(names[o])

      o += 1

else :
     print(f"Frinds Printed And Ignored Names Count Is {len(p)} ")



skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
     
    print(*skills, sep="\n") ; break

# (*)  in line 71 unpacks the list and sep work as seperator 


