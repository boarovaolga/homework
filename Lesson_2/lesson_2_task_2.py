def is_year_leap(year):
    return "Да" if year % 4 == 0 else "Нет"


ye = int(input("Введите год: "))
result = is_year_leap(ye)
print(f"Високосный ли год {ye}? - {result}")
