#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/25 6:01 PM
# @Author: wisdom
# @File:letterCombination.py


def letterCombination(digits: str) -> list:
    KEY = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if digits == '':
        return []
    ans = ['']
    for num in digits:
        if num not in KEY.keys():
            return ['']
            break
        else:
            ans = [pre + suf for pre in ans for suf in KEY[num]]
    return ans


if __name__ == '__main__':
    print('letter combination')
    digits = input()
    print(letterCombination(digits))
