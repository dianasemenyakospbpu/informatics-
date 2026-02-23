breeding_ground = input('Введите название питательной среды: ')
concentration = input('Введите концентрацию агара (%): ')
temperature = input('Введите температуру стерилизации (°C): ')

with open("C:\\Users\\User\\Documents\\semenyako_dd\\projects_2\\task_2_3\\recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f'\t{breeding_ground}')
    recipe.write(f"\nКонцентрация агара (%):\t{concentration}\n")
    recipe.write(f"Температура стерилизации (°C):\t{temperature}\n")

print("Файл 'recipe.txt' успешно сформирован!")