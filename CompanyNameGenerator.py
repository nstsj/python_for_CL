import random

names = ["пром", "агро", "торг", "урал", "север", "юг", "техно",
         "экспо", "метал", "нефть", "сельхоз", "фарм", "строй",
         "кредит", "алмаз", "-девелопмент", "развитие", "мос",
         "рос", "кубань", "сибирь", "восток", "нано", "софт",
         "микро", "онлайн", "инвест", "текстиль", "цемент"]

org_types = ["ГУП", "ООО", "ПАО", "НАО", "ФГУП", "Артель", "ГК", "Фонд", ]

names = [name.title() for name in names]


def company_name_generator(list):
    company = ''
    for x in range(6):
        company += random.choice(names)
    return company


def full_name():
    return f"{random.choice(org_types)} \"{company_name_generator(names)}\""


for i in range(10):
    print(full_name())
