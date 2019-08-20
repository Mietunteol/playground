# https://www.codewars.com/kata/if-you-cant-sleep-just-count-sheep


def count_sheep(n):
    return ''.join(f'{x} sheep...' for x in range(1, n + 1))
