don_phenotype = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
rec_phenotype = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()
if rec_phenotype == "IV":
    if don_phenotype == "I" or don_phenotype == "IV":
        print('Переливание возможно')
    else:
        print('Переливание невозможно') 
elif rec_phenotype == "III":
    if don_phenotype == "I" or don_phenotype == "III" :
        print("Переливание возможно")
    else:
        print("Переливание невозможно")
elif rec_phenotype == "II":
    if don_phenotype == "I" or don_phenotype == "II":
        print("Переливание возможно")
    else:
        print("Переливание невозможно")
else:
    if don_phenotype == "I":
        print("Переливание возможно")
    else:
        print("Переливание невозможно")

 
 