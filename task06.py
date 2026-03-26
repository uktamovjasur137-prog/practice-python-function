def is_valid_phone_number():
    number = input("Raqam: ")

    if len(number) == 9:
        print(True)

    else:
        print(False)

is_valid_phone_number()