<?php

# https://www.codewars.com/kata/printer-errors

function printerError($s)
{
    $errors = 0;
    $min = ord('a');
    $max = ord('m');
    for ($i = 0; $i < strlen($s); ++$i) {
        $value = ord($s[$i]);
        if ($value < $min || $value > $max) {
            ++$errors;
        }
    }
    $total = strlen($s);
    return "{$errors}/{$total}";
}
