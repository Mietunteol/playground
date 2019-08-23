<?php

# https://www.codewars.com/kata/simple-fun-number-176-reverse-letter

function reverseLetter($str)
{
    return strrev(preg_replace("/[^A-Za-z]/", '', $str));
}
