#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / pow(x, abs(n))
    elif n > 0:
        return x * pow(x, n - 1)


if __name__ == '__main__':
    x = float(input("enter x: "))
    n = int(input("enter n: "))

    print(func(x, n))
