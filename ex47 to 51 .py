my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)

h = 0

for num in my_nums :

    if num % 5 == 0 :
        print(f"{h +1} => {num}") 
        h += 1

else : 
    print("All Numbers Printed")

print("*"*50)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for l in L :
    
    if l == 6 or l == 8 or l == 12 :
        continue
    print(f"{str(l).zfill(2)}")

else :
    print("All Numbers Is Printed")

print("*"*50)

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}



d = {
    "A" : 100,
    "B" : 80,
    "C" : 40
}



for rank, vlaue in my_ranks.items() :
    print(f"My Rank in {rank} Is {vlaue} This Equal {d[vlaue]} Point ")

# else :
    # print(f"total point is {sum(d[rank])}")