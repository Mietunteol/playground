# https://www.codewars.com/kata/stringy-strings


def stringy(size):
    return ''.join(str(int(not (x % 2))) for x in range(size))
