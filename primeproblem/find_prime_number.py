# -*- coding: utf-8 -*-
"""
Created on 2021/7/11 0012

@author: zhou yang
"""
from functools import wraps
import random
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        rst = func(*args, **kwargs)
        end = time.time()
        print("func:", func.__name__, func.__doc__, "程序运行时间：", end-start, ", 运行结果: ", len(rst), rst)
    return wrapper


@timer
def demo(e):
    time.sleep(random.randint(0, e))
    print("运行程序名称：", demo.__name__)
    print("hello world!")


@timer
def trial_division_1(n):
    """试除法，境界1层"""
    prime_number_list = []

    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_number_list.append(i)
    return prime_number_list


@timer
def trial_division_2(n):
    """试除法，境界2层"""
    prime_number_list = []

    for i in range(2, n):
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            prime_number_list.append(i)
    return prime_number_list


@timer
def trial_division_3(n):
    """试除法，境界3层"""
    prime_number_list = []
    if n > 1:
        prime_number_list.append(2)

    for i in range(3, n):
        if i % 2 == 0:
            continue
        for j in range(3, int(i/2)+1, 2):
            if i % j == 0:
                break
        else:
            prime_number_list.append(i)
    return prime_number_list


@timer
def trial_division_4(n):
    """试除法，境界4层"""
    prime_number_list = []

    for i in range(2, n):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime_number_list.append(i)
    return prime_number_list


@timer
def trial_division_5(n):
    """试除法，境界5层"""
    prime_number_list = []

    for i in range(2, n):
        for j in prime_number_list:
            # if j > int(i**0.5)+1:
            #     break
            if i % j == 0 and j < int(i**0.5)+1:
                break
        else:
            prime_number_list.append(i)
    return prime_number_list


@timer
def eratosthenes_of_sieve(n):
    """素数筛法求质数"""
    is_prime_number = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime_number[i]:
            for j in range(i * i, n, i):
                is_prime_number[j] = False
    return [x for x in range(2, n) if is_prime_number[x]]


trial_division_1(50000)
trial_division_2(50000)
trial_division_3(50000)
trial_division_4(50000)
trial_division_5(50000)
eratosthenes_of_sieve(50000)
