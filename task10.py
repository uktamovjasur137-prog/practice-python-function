def is_strong_password():

    while True:
        password = input("Parol: ")
        
        if len(password) < 8:
            print("Kuchliroq parol kiriting")

        else:
            print("Parol qabul qilindi")
            break

is_strong_password()

 