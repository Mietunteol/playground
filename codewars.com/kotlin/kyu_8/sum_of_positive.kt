// https://www.codewars.com/kata/sum-of-positive

fun sum(numbers: IntArray): Int {
    return numbers.filter { it > 0 }.sum();
}
