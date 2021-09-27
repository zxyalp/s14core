# -*- coding: utf-8 -*-
"""
Created on 2021/9/14 0014

@author: xing yan
"""
# -*- coding: utf-8 -*-
"""
Created on 2019/9/19

@author: yang.zhou
"""
from time import sleep, ctime
import random
from tenacity import retry, stop_after_attempt, stop_after_delay, wait_fixed, wait_random, wait_exponential, retry_if_exception_type, retry_if_result


def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, (IOError, ValueError))


# 无条件重试
@retry
def do_something_unreliable():
    t = random.randint(2, 20)
    print('rand:', t)
    if t > 5:
        sleep(1)
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


# 2. 达到重试次数停止


@retry(stop=stop_after_attempt(3))
def stop_after_3_attempts():
    t = random.randint(2, 20)
    print('rand:', t)
    if t > 5:
        sleep(1)
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


# print("stop_after_3_attempts", stop_after_3_attempts())


# 3. 达到重试时间停止
# print("达到重试时间停止", "stop_after_5_s")


@retry(stop=stop_after_delay(5), reraise=True)
def stop_after_5_s():
    t = random.randint(2, 20)
    print('rand:', t)
    if t > 5:
        sleep(1)
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


# print(stop_after_5_s())


# 4. 达到重试时间或是重试次数停止


@retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
def stop_after_5_s_or_5_retrise():
    t = random.randint(2, 20)
    print('rand:', t)
    if t > 5:
        sleep(1)
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "stop_after_5_s_or_5_retrise!"


# print(stop_after_5_s_or_5_retrise())


# 5. 重试前等待时间


@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def stop_after_wait_2_s():
    t = random.randint(2, 10)
    print('rand:', t)
    if t > 3:
        sleep(1)
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "stop_after_wait_2_s!"


# print(stop_after_wait_2_s())


# 5. 重试前等待, 随机时间


@retry(stop=stop_after_attempt(5), wait=wait_random(1, 3))
def stop_after_wait_2_s():
    t = random.randint(2, 10)
    print('rand:', t)
    if t > 3:
        sleep(1)
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "stop_after_wait_2_s!"


# print(stop_after_wait_2_s())


# 6. 重试前等待, 等待时间按指数增长, 最大间隔10s


@retry(stop=stop_after_attempt(12), wait=wait_exponential(1, 10))
def wait_exponential_1():
    print(ctime())
    t = random.randint(2, 10)
    print('rand:', t)
    if t > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "wait_exponential_1!"


# print(wait_exponential_1())


# 6. 按捕获异常重试
@retry(stop=stop_after_attempt(12), wait=wait_random(1, 3), retry=retry_if_exception_type((IOError, ValueError)))
def might_io_error():
    print(ctime())
    t = random.randint(2, 10)
    print('rand:', t)
    if 1 < t < 7:
        print('IOError')
        raise IOError("Broken sauce, everything is hosed!!!111one")
    elif 7 <= t <= 10:
        print('ValueError')
        raise ValueError("触发一个ValueError")
    else:
        return "might_io_error!"


# print(might_io_error())


# print(wait_exponential_1())


# 6. 按执行结果重试
def is_none_p(value):
    """Return True if value is None"""
    print("is_none_p", value)
    return value is None


@retry(stop=stop_after_attempt(12), wait=wait_random(1, 3), retry=retry_if_result(is_none_p))
def might_return_none():
    print(ctime())
    t = random.randint(2, 10)
    print('rand:', t)
    if 1 < t < 7:
        print('IOError')
        return IOError("Broken sauce, everything is hosed!!!111one")
    elif 7 <= t <= 10:
        print('ValueError')
        raise ValueError("触发一个ValueError")
    else:
        return "might_return_none!"


print(might_return_none())