// https://www.codewars.com/kata/printer-errors

fun printerError(s: String): String = "${s.count { it !in 'a'..'m' }}/${s.length}"
