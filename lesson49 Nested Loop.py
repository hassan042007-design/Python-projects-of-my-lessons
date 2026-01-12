#-Nested-Loop---------------------------------------------------------------------------------------------------------------

# people = ["Hassan", "Yahia", "samir", "Ali",]

# skills = ["Htlm", "Css", "JS", "Java",]

# for name in people : # Outer Loop

#     #print(f" {name}, Skills is : {skills[people.index(name)]} ") # I proud of me for slove by mysilf

#     print(f"{name} Skills is : ")
    
#     for skill in skills : # Inner Loop

#         print(skill)


peoples = {
    "Hassan" : {"Htlm" : "70%",
                "Css"  : "80%", 
                "JS"   : "100%",
                "Java" : "90%"
    },
    "Yahia" : {"Htlm" : "90%",
                "Css"  : "80%", 
                "JS"   : "60%",
                "Java" : "50%"
    },

    "Samir" : {"Htlm" : "60%",
                "Css"  : "40%", 
                "JS"   : "100%",
                "Java" : "90%"
    },

    "Ali" : {"Htlm" : "70%",
                "Css"  : "80%", 
                "JS"   : "100%",
                "Java" : "90%"
    }
}

for name in peoples :
    
    print(f"{name} Skills is : {peoples[name]}")


    # Nested loop

for name in peoples :


    print(f"{name} Skills is : ")

    for skill in peoples[name] :

        print(f" {skill.upper()} : {peoples[name][skill]}  ")
