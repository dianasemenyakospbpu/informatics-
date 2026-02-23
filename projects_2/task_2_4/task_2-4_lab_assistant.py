volume = float(input('Введите требуемый объем раствора (мл): '))
salt_mass = float(volume * 0.009)
volume_of_water = volume

with open ("C:\\Users\\User\\Documents\\semenyako_dd\\projects_2\\task_2_4\\recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write("ОТЧЕТ ПО ПРИГОТОВОЛЕНИЮ:\n")
    recipe.write("------------------------\n")
    recipe.write(f"Общий объем: {volume} мл\n")
    recipe.write(f"Масса соли: {salt_mass:.2f} г\n")
    recipe.write(f"Объем воды: {volume_of_water} мл\n")





