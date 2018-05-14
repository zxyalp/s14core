# -*- coding: utf-8 -*-
"""
Created on 2018/4/22

@author: summe
"""

import turtle


def draw_polygonal(paint, distance, steps=None, speed=None, shape="turtle", color="yellow"):
    if paint is None:
        paint = turtle.Turtle()
    paint.shape(shape)
    paint.color(color)

    if speed is not None:
        paint.speed(speed)

    if steps is None:
        paint.circle(distance)
        return

    for s in range(steps):
        paint.forward(distance)
        paint.right(360 / steps)


def draw_square(paint):
    draw_polygonal(paint, 100, 4, 2)


def draw_circle(paint):
    draw_polygonal(paint, 100, shape="arrow", color="blue")


def draw_triangle(paint):
    draw_polygonal(paint, 100, 3, 2, shape="arrow", color="blue")


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor("red")
    paint = turtle.Turtle()
    draw_square(paint)
    draw_circle(paint)

    for i in range(2, 8):
        draw_polygonal(paint, 100, i, 2)
    window.exitonclick()
