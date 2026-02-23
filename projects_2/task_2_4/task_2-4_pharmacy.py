capsules = int(input('Введите общее количество произведенных капсул: '))
capsules_in_pack = int(input('Введите количество капсул в одной упаковке: '))

full_packs = capsules // capsules_in_pack
extra = capsules % capsules_in_pack

print('---Отчет фасовочного цеха---')
print(f"Полных упаковок: {full_packs}")
print(f"Остаток капсул: {extra}")