# -*- coding: utf-8 -*-
"""装饰器演示
Created on 2017/6/24

@author: summe
"""
import random
import time

"""练习》》》给函数添加计时功能"""

'''
def test():
    time.sleep(random.randint(1, 5))
    print("hello world")
'''

"""
第一例： 不带参数的函数，最简单的装饰器。
"""


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("程序运行时间：", end-start)
    return wrapper


@timer
def test():
    time.sleep(random.randint(1, 5))
    print("hello world")


# test()

'''
解释：
语法糖：@timer
等同与
test = timer(test) = wrapper
'''

"""
第二例： 带参数的函数
"""


def timer2(func):
    def wrapper(t):
        start = time.time()
        func(t)
        end = time.time()
        print("程序运行时间：", end-start)
    return wrapper


@timer2
def test2(s):
    time.sleep(random.randint(0, s))
    print("运行程序名称：", test2.__name__)
    print("hello world")

'''
装饰器：
test2 = timer2(test) = wrapper
 
test2(s) ~ wrapper(t)
'''

# test2(3)

""""
第三例，装饰器，装饰不定参数个数的函数
"""


def timer3(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("程序运行时间：", end-start)
    return wrapper


@timer3
def test3(e):
    time.sleep(random.randint(0, e))
    print("运行程序名称：", test3.__name__)
    print("hello world")


@timer3
def test4(s, e):
    if s > e:
        s, e = e, s
    time.sleep(random.randint(s, e))
    print("运行程序名称：", test4.__name__)
    print("hello world!")


@timer3
def test5(s, e, name):
    if s > e:
        s, e = e, s
    time.sleep(random.randint(s, e))
    print("运行程序名称：", test4.__name__)
    print("hello world!", name)

# test3(2)
# test4(2, 5)
# test5(1, 5, "zhoyu")


"""第四例 带参数的装饰器"""


def timer4(flag=False):
    def outer(func):
        def wrapper(*args, **kwargs):
            if flag:
                print("不打印执行时间。")
                return func(*args, **kwargs)
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print("程序运行时间：", end-start)
        return wrapper
    return outer

'''
test6 = timer4(flag='false')(test6)
'''


@timer4()
def test6(e):
    time.sleep(random.randint(0, e))
    print("运行程序名称：", test4.__name__)
    print("hello world!")


@timer4(True)
def test7(s, e, name):
    if s > e:
        s, e = e, s
    time.sleep(random.randint(s, e))
    print("运行程序名称：", test4.__name__)
    print("hello world!", name)

"""
   test6() = timer(func)(test6) = outer(test6) = wrapper(test6)
"""

# test6(2)
# test7(2, 6, "hello")

"""
第五例，修改函数属性
"""

from functools import wraps


def timer4(flag=False):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if flag:
                print("不打印执行时间。")
                return func(*args, **kwargs)
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print("程序运行时间：", end-start)
        return wrapper
    return outer


@timer4()
def test6(e):
    time.sleep(random.randint(0, e))
    print("运行程序名称：", test6.__name__)
    print("hello world!")

test6(4)
