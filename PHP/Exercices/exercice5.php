<?php
    $word = (string)readline("word : ");
    $rword = strrev($word);
    if ($word == $word) {
        echo "$word is a palindrome\n";
    }
    else {
        echo "$word is not a palindrome\n";
    }
?>
