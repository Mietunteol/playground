// https://www.codewars.com/kata/vowel-count

fun getCount(str: String): Int {
    return str.sumBy { it -> if ("AEIOUaeiou".indexOf(it) != -1) 1 else 0 }
}
