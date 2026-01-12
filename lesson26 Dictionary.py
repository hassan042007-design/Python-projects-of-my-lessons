# Dictionary----------------------------------------------------------------------------------------------------------------
# Dict Items Are Enclosed in Cyrly Braces 
# Dict Item Are Contains Key : Value
# Dict key Need To Be Immutable (Nums, String, Tuple) List Not Allowed 
# Dict Value Can Have Any Data Types
# Dict Key Must Be Unique  
# Dict is Not Ordered You Access Its Element with Key
# Dict.Keys() : will print all keys of dict
# Dict.Values() : will print all Values of dict
# Can make Dict In The Dict 
# Can Creat Dict Form Variables


user = { 
    "name" : "Hassan",
    "age" : 18,
    "country" : "Egypt",
    "Skils" : ["Html", "Css", "Java sctipt"],
    "rating" : 10.5,
    "name" : "Ahmed"
    
}

print(user)
print(user["country"])
print(user.get("country"))

print("=" *40) #Seprator

print(user.keys()) # print all keys of dictionary
print(user.values()) # print all Values of dictionary

print("=" *40) #Seprator


# Two-Dimensions Dictionary

language = { 
    "One" : {
        "name" : "Html",
        "progress" : "80%"
    },
    "Two" : {
        "name" : "Css",
        "progress" : "90%"
    },
    "Three" : {
        "name" : "Js",
        "progress" : "90"
    }
}

print(language)
print(language["One"])

print(language["Three"])
print(language["Three"]["progress"])
print(language["Three"]["name"])

print(len(language))
print(len(language["One"]))
print(len(language["Two"]))

print("=" *40) #Seprator


# Creat Dict Form Variables

frameworkOne = {
    "name" : "VueJs",
    "progress" : "70%"
} 
frameworkOne = {
    "name" : "VueJs",
    "progress" : "70%"
} 
frameworkTwo = {
    "name" : "ReactJs",
    "progress" : "100%"
} 
frameworkThree = {
    "name" : "Angular",
    "progress" : "90%"
} 

Allframework = {
    "One" : frameworkOne,
    "Two" : frameworkTwo,
    "Three" : frameworkThree
}

print(Allframework)
print(Allframework.keys())
print(Allframework.values())