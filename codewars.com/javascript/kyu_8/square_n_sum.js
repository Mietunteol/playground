// https://www.codewars.com/kata/square-n-sum

function squareSum(numbers) {
    return numbers.map(x => Math.pow(x, 2)).reduce((a, b) => a + b, 0);
}
