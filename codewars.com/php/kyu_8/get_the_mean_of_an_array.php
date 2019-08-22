<?php

# https://www.codewars.com/kata/get-the-mean-of-an-array

function get_average($a)
{
    return intval(array_sum($a) / count($a));
}
