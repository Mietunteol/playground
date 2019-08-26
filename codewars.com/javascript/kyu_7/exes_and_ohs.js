// https://www.codewars.com/kata/exes-and-ohs

const XO = (str) =>
    str.toLowerCase().split('').filter(x => x === 'x').length
    ===
    str.toLowerCase().split('').filter(x => x === 'o').length;
