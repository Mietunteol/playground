# https://www.codewars.com/kata/mumbling


def accum(s):
    result = []
    for i, c in enumerate(s):
        result.append(f'{c.upper()}{c.lower() * i}')
    return '-'.join(result)
