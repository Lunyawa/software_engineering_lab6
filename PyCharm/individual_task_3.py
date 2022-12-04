#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите предложение: ")
    letter = input("Введите букву, которая будет стоять перед и: ")

    if len(letter) > 1:
        print(
            "Нужно было ввести одну букву!!",
            file=sys.stderr
        )
        exit(1)

    if s[-1] != '.':
        print(
            "В конце предложения нужно было поставить точку!!!",
            file=sys.stderr
        )
        exit(1)

    temp = s.rfind('и')
    if temp == -1:
        print(
            "Буква 'и' не была найдена",
            file=sys.stderr
        )
        exit(1)

    new_s = s[:temp] + letter + s[temp:]

    print(new_s)
