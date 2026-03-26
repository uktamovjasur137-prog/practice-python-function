def check_guess():
    num = 7
    while True:
        guess_num = int(input("Son: "))
        
        if num > guess_num:
            print("Kattaroq son")

        elif num < guess_num:
            print("Kichikroq son")

        else:
            print("Topdingiz")
            break 
             
check_guess()