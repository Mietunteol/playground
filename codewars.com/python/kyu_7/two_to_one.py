# https://www.codewars.com/kata/two-to-one


def longest(s1, s2):
    return ''.join(sorted(list(set(s1 + s2))))
