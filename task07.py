def ask_question_and_answer():
    answer = 8
    print("Savol: Quyosh sistemasida nechta sayyora bor?")
    user_answer = int(input("Javob: "))

    if answer == user_answer:
        print(True)
    else:
        print(False)

ask_question_and_answer()

