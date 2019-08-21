# https://www.codewars.com/kata/alternate-capitalization


def capitalize(s):
    odd = []
    even = []
    for i, c in enumerate(s):
        odd.append(c.lower() if i % 2 else c.upper())
        even.append(c.lower() if not i % 2 else c.upper())
    return [''.join(odd), ''.join(even)]
