def age_calculate():
    now = 2026
    age = int(input("Yilingiz: "))

    result = now - age
    return result

birth_year = age_calculate()
print(birth_year)

age = 2026 - birth_year

if age >= 18:
    print("Siz balogatga yetgansiz")
else:
    print("Siz balogatga yetmagansiz")