// https://www.codewars.com/kata/century-from-yea

function century(year) {
    let quotient = Math.floor(year / 100);
    let remainder = year % 100;
    return quotient + (remainder === 0 ? 0 : 1);
}
