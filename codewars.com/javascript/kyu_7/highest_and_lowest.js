// https://www.codewars.com/kata/highest-and-lowest

function highAndLow(numbers) {
    numbers = numbers.split(' ');
    let high = Math.max(...numbers.map(x => parseInt(x, 10)));
    let low = Math.min(...numbers.map(x => parseInt(x, 10)));
    return `${high} ${low}`;
}
