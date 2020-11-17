# генератор названий компаний

import random

names = ["пром", "агро", "торг", "урал", "север", "юг", "техно",
         "экспо", "метал", "нефть", "сельхоз", "фарм", "строй",
         "кредит", "алмаз", "-девелопмент", "развитие", "мос",
         "рос", "кубань", "сибирь", "восток", "нано", "софт",
         "микро", "онлайн", "инвест", "текстиль", "цемент"]

org_types = ["ГУП", "ООО", "ПАО", "НАО", "ФГУП", "Арт", "ГК", "Фонд", ]

names = [name.title() if not name.startswith("-") else name for name in names]

def full_company_name():
    def company_name_generator(list):
        company = ''
        for x in range(6):
            company += random.choice(names)
        return company
    return f"{random.choice(org_types)}\t\"{company_name_generator(names)}\""

for i in range(20):
    print(full_company_name())

# запустите ячейку несклько раз