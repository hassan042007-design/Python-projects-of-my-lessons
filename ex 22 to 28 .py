nums = [1, 2, 3, 3, 4, 5, 1]
list_unique = set(nums)
print(list_unique)
list_unique = list(list_unique)
print(list_unique)
list_unique.remove(5)
print(list_unique)


Set = {1, 2, 3}
Set2 = {"A", "B", "c"}

print(Set.union(Set2))
print(Set|Set2)
Set.update(Set2)
print(Set)

Set3 ={1, 2, 3}
print(Set3) 
Set3.clear()
print(Set3) 
Set3.add("A")
Set3.add("B")
print(Set3) 
Set3.discard("c")
print(Set3) 

Set_1 = {1, 2, 3}
Set_2 = {1, 2, 3, 4, 5, 6}
print(Set_1.issubset(Set_2))



skill = {
    "first" : {
    "HTMl" : "Progress Is 90%",
    },
    "second" : {
    "CSS"  : "progress is 80% "
    }
}
print(skill["first"])
print(skill["second"])

AI = {
   "AI" : "progress is 20%" 
}
skill.update({"third" : AI} )
print(skill["third"])

w = {
    "name" : "java",
    "defcult" : "medium"
}

w["and"] = "c"
print(w)
w.update({"name" : "c++"})



