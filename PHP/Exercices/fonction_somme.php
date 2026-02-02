<?php
    function summ($n) {
        for ($i=1; $i <= $n; $i++) {
            $tab[] = $i;
        }
        return array_sum($tab);
    }
    echo "n : ";
    $n = (int)readline("n : ");
    $sum = summ($n);

    echo $sum."\n";