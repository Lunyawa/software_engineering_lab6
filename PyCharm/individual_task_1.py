#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")

    if s.count('м') or s.count('н'):
        print(s.count('м') * 'м' + s.count('н') * 'н')
    else:
        print("Букв м и н нет в этом предложении!")
