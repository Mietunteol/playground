# https://www.codewars.com/kata/is-it-a-palindrome


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i].lower() != s[len(s) - i - 1].lower():
            return False
    return True
