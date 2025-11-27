value = input("Please enter a number: ")

value_as_int = ""

# for character in value:
for i in range(len(value)):
    # if character in "0123456789":
    print(i, value[i])
    if value[i] in "0123456789":
        # value_as_int = value_as_int + character
        value_as_int = value_as_int + value[i]
    else:
        # print("Invalid character")
        print("Invalid character at position " + str(i))


print(value)