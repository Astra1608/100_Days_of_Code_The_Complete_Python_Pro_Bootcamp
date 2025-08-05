programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
#retrive
print(programming_dictionary["Bug"])
#double quote imp for numbers simple number  no double quote in key
programming_dictionary["Loop"] = "The action of doing repeatative work"
print(programming_dictionary)
#empty dict
empty_dic = {}
#wipe existing dict
#programming_dictionary = {}
#print(programming_dictionary)
#edit an item in a cdict
programming_dictionary["Bug"]="A moth in a computer"
print(programming_dictionary)
#loop through dict
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

