<?php
    function summ($n) {
        for ($i=1; $i <= $n; $i++) {
            $tab[] = pow($i, 2);
        }
        return array_sum($tab);
    }
    echo "n : ";
    $n = (int)readline("n : ");
    $sum = summ($n);
    echo $sum."\n";