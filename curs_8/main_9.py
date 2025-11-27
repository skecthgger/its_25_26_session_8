list_of_names = [
    "sheila", "lilo",
    "marcela", "ana", "eva",
    "florin", 'alex', "petre",
    [
        "lili",
        "radu",
        [
            "matei",
        ]
    ]
]


if "matei" in list_of_names:
    print("No matei is found")
else:
    print("No matei is not found")
    if isinstance(list_of_names[8], list) and "matei" in list_of_names[8]:
        print("No matei is found")
    else:
        print("No matei is not found")
        if isinstance(list_of_names[8][1], list) and "matei" in list_of_names[8][1]:
            print("No matei is found")
        else:
            print("No matei is not found")
            print(isinstance(list_of_names[8][1], list) )