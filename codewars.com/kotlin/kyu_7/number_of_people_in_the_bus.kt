// https://www.codewars.com/kata/number-of-people-in-the-bus

fun people(busStops: Array<Pair<Int, Int>>): Int {
    return busStops.fold(0) { sum, element -> sum + element.first - element.second }
}
