// https://www.codewars.com/kata/count-the-digit

package countdig

fun nbDig(n: Int, d: Int): Int = (0..n).map { it * it }.joinToString("").filter { "$it" == "$d" }.count()
