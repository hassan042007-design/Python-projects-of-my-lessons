# Advanced-Dectionary------------------------------------------------------------------------------------
# Take Automaticly First Object in key and second in value 
# 


mySkills = {
    "Html" : "80",
    "Css" : "70",
    "JS" : "100",
    "PHP" : "90"
}


# old sytle 
# for skill in mySkills :

#     print(f"{skill} => {mySkills[skill]}")


# Advanced Way :

for skill_key, skill_progress in mySkills.items() :
    
    print(f"{skill_key} => {skill_progress}")


print("*"*50)

myUltimateskills = {
    "HTML" : {
        "Main" : "80%",
        "pugjs" : "80%"
    },

    "CSS" : {
        "Main" : "90%",
        "Sass" : "70%"

    }
}

for main_key , main_value in myUltimateskills.items() :

    print(f"{main_key} Progress Is:")

    for child_key, child_value in main_value.items() :

        print(f"{child_key} => {child_value}")

        