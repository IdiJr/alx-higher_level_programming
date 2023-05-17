#!/usr/bin/python3


def to_subtract(list_num):
    max_list = max(list_num)
    return max_list - sum(n for n in list_num if max_list > n)


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_rom = 0
    list_num = [0]

    for i in roman_string:
        if i in rom_n:
            if rom_n[i] > last_rom:
                list_num[-1] = rom_n[i] - list_num[-1]
            else:
                list_num.append(rom_n[i])
            last_rom = rom_n[i]

    num = sum(list_num)
    return (num)
