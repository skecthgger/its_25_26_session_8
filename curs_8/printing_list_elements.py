list_of_names = [
    "sheila", "lilo", "matei",
    "marcela", "ana", "eva",
    "florin", 'alex', "petre"
]

my_string = ""

#Iterating over list elements
for name in list_of_names:
    #Print the item from the list
    # print(name)
    my_string = my_string + " " + name
    print(my_string)

print(my_string)
