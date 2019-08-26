// https://www.codewars.com/kata/vowel-count

const getCount = (str) => str
    .split('')
    .filter(x => ['a', 'e', 'i', 'o', 'u'].indexOf(x.toLowerCase()) !== -1)
    .length;
