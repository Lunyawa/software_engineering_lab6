#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    words = input("Введите три слова: ").lower().split()

    # Выдает ошибку если не 3 слова
    if len(words) > 3 or len(words) < 3:
        print(
            "Введено не три слова",
            file=sys.stderr
        )
        exit(1)

    # Находим повторяющееся буквы
    letters = set()
    for i in words[0]:
        if (i not in letters) and (i in words[1]) and (i in words[2]):
            letters.add(i)

    # Выводим повторяющееся буквы
    if len(letters) == 0:
        print("Общих букв нет")
    else:
        print(f"Буквы которые повторяются -> {', '.join(letters)}")