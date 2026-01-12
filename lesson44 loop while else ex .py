# loop while and else traning 
# While condition is True code will Run until condition Become False


myF = ["Ha", "Os", "Sa", "Qi", "Ta", "Ah", "Mo"]

print(len(myF)) #list lenght


a = 0

while a < len(myF) : # a < 8

    print(myF[a])
    a += 1  # a = a + 1

else :
    print("fille is done")


myL = ["Ha", "Os", "Sa", "Qi", "Ta", "Ah", "Mo", "Za", "Kh" , "Ma"]

h = 0 
g = str(160)
while h < len(myL) :
    print(f"#{str(h + 1).zfill(len(g))} {myL[h]}")
    h += 1

else :
    print("List is done")