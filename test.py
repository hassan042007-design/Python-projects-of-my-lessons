Var = int(input())
for Lenght in range (1,Var + 1,1):
     for x in range (0,Var - Lenght,1):
         print(" ",end='')
     for y in range(0,Lenght*2-1,1):
         print ("H",end='')
     print("\n")
