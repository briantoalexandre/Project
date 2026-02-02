<?php
    $sentence = readline("type a sentence : \n");
    $size = strlen($sentence);
    if ($size < 20) {
        echo "small sentence\n";
    }
    elseif ($size > 50) {
        echo "big sentence\n";
        
    }
    else {
        echo "cool\n";
    }
?>