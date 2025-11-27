# Define database
database = {
    "dienase": "safe_password",
    "emahmut": "<PASSWORD>",
    "iberci": "even_safer_password",
    "avesca": "safe-ish-password",
    "pispir": "pass",
    "dcrisan": "PC_HARDWARE",
    "dvirban": "save",
    "atanase": "SAFEEE"
}


user = input("Enter username: ")

if user in database.keys():
    print("User found")
    # print(database.keys())
    # print(database[user])
    # print(database.values())
    # print(type(database.values()))

    password = input("Enter password: ")
    if password == database[user]:
        print("Login successful")
    else:
        print("Login failed")
else:
    new_user_flag = input("User not found. Do you want to create one? (Y/n)")
    if new_user_flag[0].lower() == "y":
        new_user = input("Enter new username: ")
        new_user_password = input("Enter new password: ")
        if new_user not in database.keys():
            # add a new value to the dictionary
            database[new_user] = new_user_password
            print(database)
        else:
            print("User already found")
    else:
        print("Buh bye")