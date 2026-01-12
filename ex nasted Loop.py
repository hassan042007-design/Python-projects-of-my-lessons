Nase = {
    "Hassan" : { "HTML" : "70%",
                 "CSS"  : "100%",
                 "Java" : "60",
                 "JS"   : "80%"
        },

    "Mohamed": { "HTML" : "80%",
                 "CSS"  : "90%",
                 "Java" : "50",
                 "JS"   : "100%" 

    }

} 


for name in Nase :

    print(f"The Member {name} Skills Is : ")

    for skills in Nase[name] :

        print(f"{skills} : {Nase[name][skills]} ")