# https://www.codewars.com/kata/covfefe


def covfefe(s):
    if s.find('coverage') != -1:
        return s.replace('coverage', 'covfefe')
    return f'{s} covfefe'
