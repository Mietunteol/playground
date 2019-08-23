<?php

# https://www.codewars.com/kata/sort-out-the-men-from-boys-1

function menFromBoys($arr)
{
    $men = [];
    $boys = [];
    foreach ($arr as $value) {
        if ($value % 2) {
            $boys[] = $value;
        } else {
            $men[] = $value;
        }
    }
    sort($men);
    rsort($boys);
    return array_merge(array_unique($men), array_unique($boys));
}
