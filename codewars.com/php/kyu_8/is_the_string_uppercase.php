<?php

# https://www.codewars.com/kata/is-the-string-uppercase

function is_uppercase($str)
{
    foreach (str_split($str) as $char) {
        if (ctype_alpha($char) && ctype_lower($char)) {
            return false;
        }
    }
    return true;
}