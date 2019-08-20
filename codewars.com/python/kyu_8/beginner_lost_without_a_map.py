# https://www.codewars.com/kata/beginner-lost-without-a-map
import functools
import operator

double = functools.partial(operator.mul, 2)


def maps(a):
    return list(map(double, a))
