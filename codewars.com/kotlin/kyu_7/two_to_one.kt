// https://www.codewars.com/kata/two-to-one

package twotoone

fun longest(s1:String, s2:String):String {
    val r : MutableSet<Char> = mutableSetOf()
    r.addAll(s1.toCharArray().toMutableSet())
    r.addAll(s2.toCharArray().toMutableSet())
    return r.toList().sorted().joinToString("")
}
