def is_palindrome():
    text = input("So‘z: ")

    if text == text[::-1]:
        print(True)
    else:
        print(False)

is_palindrome()