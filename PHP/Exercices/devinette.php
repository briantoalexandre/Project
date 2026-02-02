<?php
    $r = rand(0, 100);
    $i = 6;
    while (true) {
        $n = (int)readline("n = ");
        $i--;
        echo "tries left : ".($i)."\n";
        if ($n > $r) {
            echo "lower\n";
        }
        elseif ($n < $r) {
            echo "greater\n";
        }
        elseif ($n == $r) {
            echo "\nwon\n";
            break;
        }
        if ($i < 1) {
            echo "\nloose, $r was the number\n";
            break;
        }
    }
?>