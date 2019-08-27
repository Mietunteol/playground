// https://www.codewars.com/kata/find-the-smallest-integer-in-the-array

package solution

class SmallestIntegerFinder {

    fun findSmallestInt(nums: List<Int>): Int {
        return nums.min()!!;
    }

}