<?php

# https://www.codewars.com/kata/form-the-minimum

function minValue($arr)
{
    $result = array_unique($arr);
    sort($result);
    return intval(join('', $result));
}
