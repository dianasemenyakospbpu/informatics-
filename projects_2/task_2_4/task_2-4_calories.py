proteins = input('Введите массу белка в продукте (г): ')
prot = float(proteins)
fats = input("Введите массу жиров в продукте (г): ")
fat = float(fats)
carbs = input('Введите массу углеводов в продукте(г): ')
carb = float(carbs)

calories = float(prot * 4 + fat * 9 + carb * 4)

print(f'Калорий в продукте: {calories}')