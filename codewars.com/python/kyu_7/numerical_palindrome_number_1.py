# https://www.codewars.com/kata/numerical-palindrome-number-1


def palindrome(num):
    if not isinstance(num, int):
        return 'Not valid'
    if num <= 0:
        return 'Not valid'
    return str(num) == str(num)[::-1]