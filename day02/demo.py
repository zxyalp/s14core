# -*- coding: utf-8 -*-
"""
练习： 购物练习程序
需求：
    1、启动程序后，让用户输入工资，然后打印商品列表
    2、允许用户根据商品编号购买商品
    3、用户选择商品后，检测余额是否足够，够就直接扣款，不够给出提示
    4、可以随时退出，退出时，打印已购买商品和余额

Created on 2017/6/3

@author: summe
"""

merchandise = [('苹果手机', 5280), ('小米手机', 1999), ('毛皮大衣', 900), ('编程原理.PDF', 89),
               ('微波炉', 399), ('安莫希酸奶', 65)]


user = []


pro_list = '''
================商品列表=============
1、苹果手机         5280
2、小米手机         1999
3、毛皮大衣         900
4、编程原理.PDF     89
5、微波炉           399
6、安莫希酸奶       65
'''
wages = int(input("请输入你的工资（人民币）："))

while True:
    money = wages
    print(pro_list.isdigit())
    num = int(input("请选输入商品编号（0表示退出）>>>"))-1
    if money-merchandise[num][1] >= 0:
        user.append(merchandise[num][0])
        money = money-merchandise[num][1]
    else:
        print("账号余额不足")
    if num == 'q':
        break
    print("已购买商品：", user)
    print("余额：", money)

