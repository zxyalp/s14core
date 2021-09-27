# -*- coding: utf-8 -*-
"""
Created on 2021/9/4 0004

@author: xing yan
"""
import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc:
    def __init__(self, func, args, name=''):
        self.func = func
        self.args = args
        self.name = name

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at: ', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at: ', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at: ', ctime())


if __name__ == '__main__':
    main()