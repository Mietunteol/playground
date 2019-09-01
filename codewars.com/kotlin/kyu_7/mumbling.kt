// https://www.codewars.com/kata/mumbling

package accum

fun accum(s: String): String {
    return s
        .mapIndexed() { i, e -> "${e.toUpperCase()}${e.toLowerCase().toString().repeat(i)}" }
        .joinToString("-")
}
