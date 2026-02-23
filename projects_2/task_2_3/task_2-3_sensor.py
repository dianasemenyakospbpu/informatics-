operator_name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")

with open("C:\\Users\\User\\Documents\\semenyako_dd\\projects_2\\task_2_3\\sensor_log.txt", "a", encoding="utf-8") as sensor:
    sensor.write(f"{operator_name}")
    sensor.write(f"\t{pressure} (Па)\n")

print('Данные успешно сохранены в sensor_log.txt')