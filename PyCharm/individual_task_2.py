#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите последовательность слов: ")

    # делаем новую строку с правильным написанием
    new_s = s.replace("чя", "ча")
    new_s = new_s.replace("щя", "ща")

    if new_s == s:
        print("Вы написали последовательность слов правильно!!!")
    else:
        print(f"Исправленная последовательность слов -> {new_s}")