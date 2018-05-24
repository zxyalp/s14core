# -*- coding: utf-8 -*-

import math
from decimal import Decimal, getcontext
from functools import reduce


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates


# 向量加法
def add(*args):
    return [x+y for x, y in zip(*args)]


# 向量减法
def minus(*args):
    return [x-y for x, y in zip(*args)]


# 标量乘法
def scalar_multiply(c, v):
    return [c*x for x in v]


# 计算向量大小
def calc_vector_size(v):
    return math.sqrt(sum([x**2 for x in v]))


# 单位向量
def unit_vector(v):
    try:
        return scalar_multiply(1.0/calc_vector_size(v), v)
    except ZeroDivisionError:
        raise Exception('Cannot normalize the zero vector.')


# 计算弧度
def angle_with_radian(*args):
    try:
        return math.acos(dot_product(*args)/reduce(lambda x, y: x*y, [calc_vector_size(v) for v in args]))
    except ZeroDivisionError:
        raise Exception('Cannot normalize the zero vector.')


# 计算角度
def angle_with_degree(*args):
    return angle_with_radian(*args)*180.0/math.pi


# 向量内积 v*w
def dot_product(*args):
    return sum([reduce(lambda x, y: x*y, item) for item in zip(*args)])


# parallel 平行向量  parallel component 平行分量
def is_parallel_to(*vectors):
    return is_zero(*vectors) or angle_with_radian(*vectors) in [0, math.pi]


def is_zero(*vectors, tolerance=1e-10):
    for v in vectors:
        if calc_vector_size(v) < tolerance:
            return True
    return False


# 正交向量   perpendicular component 正交分量
def is_orthogonal_to(*vectors, tolerance=1e-10):
    return abs(dot_product(*vectors)) < tolerance


# 计算向量投影b为基向量，V向量为投影向量
def component_parallel_to(v, b):
    return scalar_multiply(dot_product(v, unit_vector(b)), unit_vector(b))


# 计算b基向量的正交向量v-t
def component_orthogonal_to(v, b):
    return minus(v, component_parallel_to(v, b))


# 计算vxw的向量积
def cross_products(v, w):
    try:
        x_1, y_1, z_1 = v
        x_2, y_2, z_2 = w
        return [y_1*z_2 - y_2*z_1, -(x_1*z_2-x_2*z_1), x_1*y_2 - x_2*y_1]
    except ValueError as e:
        msg = str(e)
        if msg == "not enough values to unpack (expected 3, got 2)":
            v.append(0)
            w.append(0)
            return cross_products(v, w)
        elif (msg == "too many values to unpack (expected 3)" or
              "not enough values to unpack" in msg):
            raise Exception("仅支持二维或是三维坐标系")
        else:
            raise e


# 计算向量v,w的平行四边形面积
def area_parallelogram(v, w):
    return calc_vector_size(cross_products(v, w))


# 计算向量v,w的三角形面积
def area_triangle(v, w):
    return area_parallelogram(v, w)/2.0


# 如果向量只有x,y。则添加z=0.
def two_trans_three_dimensional(*coordinates):
    for coordinate in coordinates:
        if len(coordinates) < 3:
            coordinate.append(0)


# print(math.sqrt(16))
# print(add([8.218, -9.341], [-1.129, 2.111]))
# print(subtract([7.119, 8.215], [-8.223, 0.878]))
# print(scalar_multiply(7.41, [1.671, -1.012, -0.318]))
#
#
# print(calc_vector_size([-0.221, 7.437]))
# print(calc_vector_size([8.813, -1.331, -6.247]))
# print(unit_vector([5.581, -2.136]))
# print(dot_product([1, 2, 3, 5], [4, 5, 6,9], [7, 8, 9,10]))
#
# print(calc_angle_radian([1, 2, 3], [4, 5, 6]))
# print(calc_angle_degree([1, 2, -1], [3, 1, 0]))


# print(dot_product([7.887, 4.138], [-8.802, 6.776]))
# print(dot_product([-5.955, -4.904, -1.874], [-4.496, -8.755, 7.103]))
#
# print(angle_with_radian([3.183, -7.627], [-2.668, 5.319]))
# print(angle_with_degree([7.35, 0.221, 5.188], [2.751, 8.259, 3.985]))
#
#
# print(check_vector_parallel([1, 2, 3], [0, 0, 0]))

# print(is_parallel_to([-7.579, -7.88], [22.737, 23.64]))
# print(is_orthogonal_to([-7.579, -7.88], [22.737, 23.64]))
#
#
# print(is_parallel_to([-2.029, 9.97, 4.172], [-9.231, -6.639, -7.245]))
# print(is_orthogonal_to([-2.029, 9.97, 4.172], [-9.231, -6.639, -7.245]))
#
#
# print(is_parallel_to([-2.328, -7.284, -1.214], [-1.821, 1.072, -2.94]))
# print(is_orthogonal_to([-2.328, -7.284, -1.214], [-1.821, 1.072, -2.94]))
#
#
# print(is_parallel_to([2.118, 4.827], [0, 0]))
# print(is_orthogonal_to([2.118, 4.827], [0, 0]))

# print(component_parallel_to([3.039, 1.879], [0.825, 2.036]))
# print(component_orthogonal_to([-9.88, -3.264, -8.159], [-2.155, -9.353, -9.473]))
#
#
# print(component_parallel_to([3.009, -6.172, 3.692, -2.51], [6.404, -9.144, 2.759, 8.718]))
# print(component_orthogonal_to([3.009, -6.172, 3.692, -2.51], [6.404, -9.144, 2.759, 8.718]))


# print(cross_products([8.462], [6.984]))

print(area_parallelogram([-8.987, -9.838, 5.031], [-4.268, -1.861, -8.866]))

print(area_triangle([1.5, 9.547, 3.691], [-6.007, 0.124, 5.772]))
