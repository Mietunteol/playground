<?php

# https://www.codewars.com/kata/parts-of-a-list

function partlist($arr)
{
    $result = [];
    for ($i = 1; $i < count($arr); ++$i) {
        $result[] = [
            join(' ', array_slice($arr, 0, $i)),
            join(' ', array_slice($arr, $i))
        ];
    }
    return $result;
}
