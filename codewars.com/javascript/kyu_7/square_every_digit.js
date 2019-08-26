// https://www.codewars.com/kata/square-every-digit

const squareDigits = (num) => parseInt(
    num
        .toString()
        .split('')
        .map(x => (parseInt(x, 10) ** 2).toString())
        .join(''),
    10
);