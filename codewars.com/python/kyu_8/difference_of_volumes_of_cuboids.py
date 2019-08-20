# https://www.codewars.com/kata/difference-of-volumes-of-cuboids
import functools


def find_difference(a, b):
    volume_a = functools.reduce(lambda x, y: x * y, a)
    volume_b = functools.reduce(lambda x, y: x * y, b)
    return abs(volume_a - volume_b)
