def get_grade():
    score = int(input("Ball(0 dan 100 gacha): "))

    if 75 <= score <= 100:
        print("Balingiz: A")

    elif 50 <= score < 75:
        print("Balingiz: B")

    elif 25 <= score < 50:
        print("Balingiz: C")

    elif 0 <= score < 25:
        print("Balingiz: F")

    else:
        print("Notogri ball")

get_grade()