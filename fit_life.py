# 1. Знакомство
user_name = input("Введите ваше имя: ")
print(f"Привет, {user_name}!")
# запрос возраста и сохранение в переменную user_age с преобразованием в число
user_age = int(input("Введите ваш возраст: "))
# 2. Сбор данных. Запрос веса (в кг) и сохранение в user_weight (тип float)
user_weight = float(input("Введите ваш вес (в кг): "))
# Запрос роста (в метрах, например 1.75) и сохранение в user_height (тип float)
user_height = float(input("Введите ваш рост (в метрах, например 1.75): "))
# 3. Рассчет bmi: вес разделить на рост в квадрате (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)
# Подсчет воды: вес * 30 мл и сохранение в water_needed
WATER_PER_KG_ML = 30
water_needed_ml = user_weight * WATER_PER_KG_ML
# перевод мл в л
WATER_PER_KG_L = 1000
water_needed_l = water_needed_ml / WATER_PER_KG_L
# 4. Вывод результата
print(f"{'-' * 35}")
print(f"Отчет для пользователя: {user_name}")
print(f"Возраст: {user_age} лет")
print(f"ИМТ: {bmi}")
print(f"Норма воды: {water_needed_l} литров в день")
print()
print("Расчет окончен. Будьте здоровы!")
print(f"{'-' * 35}")