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

    print(f"{name} has Skills Is : ")
    
    for skill in peoples[name] :
        print(f"{skill.upper()} : {peoples[name][skill]}")