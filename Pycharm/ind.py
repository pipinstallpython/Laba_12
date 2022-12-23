#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, abs(n))
    elif n > 0:
        return x * power(x, n - 1)


def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(a, n / 2) ** 2
    else:
        return a * power(a, n - 1)


if __name__ == '__main__':
    x = float(input("enter x: "))
    n = int(input("enter n: "))

    print(func(x, n))
