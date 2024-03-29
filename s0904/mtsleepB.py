# -*- coding: utf-8 -*-
"""
Created on 2021/9/4 0004

@author: xing yan
"""
import _thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at: ', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at: ', ctime())
    lock.release()


def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        look = _thread.allocate_lock()
        look.acquire()
        locks.append(look)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print('all done at: ', ctime())


if __name__ == '__main__':
    main()