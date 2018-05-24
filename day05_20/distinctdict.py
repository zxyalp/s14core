# -*- coding: utf-8 -*-
"""
Created on 2018/5/20

@author: xing yan
"""


class DistinctError(ValueError):
    """如果向distinctdict添加重复值， 则向这个这个错误."""


class distinctdict(dict):
    """不接受重复的字典值。"""
    def __setitem__(self, key, value):
        if value in self.values():
            if key in self and self[key] != value or key not in self:
                raise DistinctError("This value already exists for different key.")
        super().__setitem__(key, value)


my = distinctdict()

my["name"] = "zhansan"
my["name1"] = "zhansan1"

print("name" in my)

