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
        func(*args, **kwargs)
        end = time.time()
        print("func:", func.__name__, func.__doc__, "程序运行时间：", end-start)
    return wrapper


@timer
def demo(e):
    time.sleep(random.randint(0, e))
    print("运行程序名称：", demo.__name__)
    print("hello world!")


@timer
def trial_division_1(n):
    """试除法，境界1层"""
    pass

@timer
def trial_division_1(n):
    """试除法，境界2层"""
    pass

@timer
def trial_division_1(n):
    """试除法，境界3层"""
    pass


@timer
def trial_division_1(n):
    """试除法，境界4层"""
    pass


@timer
def trial_division_1(n):
    """试除法，境界5层"""
    pass


@timer
def eratosthenes_of_sieve(n):
    """素数筛法求质数"""
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    prime_name_list = [x for x in range(2, n + 1) if IsPrime[x]]
    # print(prime_name_list)

eratosthenes_of_sieve(500000)

print([True] * (10 + 1))
print(4 ** 0.5)
