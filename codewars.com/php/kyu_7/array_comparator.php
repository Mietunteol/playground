<?php

# https://www.codewars.com/kata/array-comparator

function match_arrays(array $a, array $b): int
{
    return count(array_intersect($b, $a));
}
