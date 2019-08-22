<?php

# https://www.codewars.com/kata/count-by-x

function countBy($x, $n)
{
    $result = [$x];
    $i = 1;
    while ($i < $n) {
        $result[] = end($result) + $x;
        $i++;
    }
    return $result;
}
