// https://www.codewars.com/kata/maximum-length-difference

package maxlendiff

import kotlin.math.max
import kotlin.math.abs

fun mxdiflg(a1: Array<String>, a2: Array<String>): Int {
    var r = -1
    for (e1 in a1)
        for (e2 in a2)
            r = max(r, abs(e1.length - e2.length))
    return r
}
