<?php

# https://www.codewars.com/kata/get-the-middle-character

function getMiddle($text)
{
    $middle = intdiv(strlen($text), 2);
    return strlen($text) % 2 ? $text[$middle] : substr($text, $middle - 1, 2);
}
