#!/usr/bin/python3

# Test phrase: Съешь же ещё этих мягких французских булок да выпей чаю
charbase = {"а": "a", "б": "b", "в'": "w", "в": "v", "г": "g", "д": "d",
            "е": "e", "ё": "yo", "ж": "zh", "з": "z", "и": "i", "й": "i",
            "к'": "q", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
            "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f",
            "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "``",
            "ы": "y", "ь": "`", "э": "e", "ю": "yu", "я": "ya", " ": " ",
            "\"": "\"", ".": ".", "(": "(", '\\': "\\", ")": ")",
            ":": ":", ";": ";", ",": ","}

while True:
    original_word = input("Введите слово: (введите пустую строку для прекращения программы) ")
    if original_word == "":
        break

    print("Вы ввели:", original_word)
    original_word = list(original_word)
    translit = []

    for i in original_word:
        if i not in charbase:
            translit.append(i)
            print(i+":", "Предупреждаю! Кажется, это не русский алфавит.")
            continue

        if i.isupper():
            i = charbase.get(i.lower())
            i = i.upper()
            translit.append(i)
        else:
            i = charbase.get(i)
            translit.append(i)
    result_word = "".join([i for i in translit])
    print("\n", "Вот, что получилось в итоге:", result_word, "\n")
    continue
