<?php
    function prod($n) {
        $k = 1;
        for ($i=1; $i <= $n; $i++) {
            $k *= $i;
        }
        return $k;
    }
    echo "n : ";
    $n = (int)readline("n : ");
    $sum = prod($n);

    echo "$n! = $sum\n";