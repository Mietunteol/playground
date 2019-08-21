# https://www.codewars.com/kata/remove-duplicate-words


def remove_duplicate_words(s):
    result = []
    for word in s.split(' '):
        if word not in result:
            result.append(word)
    return ' '.join(result)
