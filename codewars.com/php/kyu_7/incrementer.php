<?php

# https://www.codewars.com/kata/incrementer

function incrementer($nums)
{
    if (empty($nums)) {
        return [];
    }
    $i = 1;
    foreach ($nums as &$value) {
        $value += $i;
        if ($value >= 10) {
            $value = substr((string)$value, -1);
        }
        $i++;
    }
    return $nums;
}
