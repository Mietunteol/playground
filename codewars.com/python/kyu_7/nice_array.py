# https://www.codewars.com/kata/nice-array


def is_nice(arr):
    if not arr:
        return False
    for value in arr:
        if value + 1 in arr:
            continue
        if value - 1 in arr:
            continue
        return False
    return True
