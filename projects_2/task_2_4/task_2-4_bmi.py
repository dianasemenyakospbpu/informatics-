weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))
right_height = float(height / 100)

bmi = weight / (right_height ** 2)

print('\n---Отчет о состоянии здоровья---')
print(f'Рост:\t{height} см')
print(f'Вес:\t{weight} кг')
print(f"Индекс массы тела: {bmi:.2f}")