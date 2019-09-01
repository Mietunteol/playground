// https://www.codewars.com/kata/highest-and-lowest

fun highAndLow(numbers: String): String {
    var n = numbers.split(" ").map { it -> it.toInt() }
    return "${n.max()} ${n.min()}"
}
