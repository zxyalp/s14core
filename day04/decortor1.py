# -*- coding: utf-8 -*-
"""练习： 用户登录权限验证

1、首页，不需要登录
2、后台管理
Created on 2017/6/18

@author: summe
"""


def auth(func):
    def wrapper():
        pass


@auth
def index():
    print("hello 欢迎登录飞鱼超市！")


@auth
def manager():
    print("个人信息资料修改")
