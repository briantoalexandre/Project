<?php
    function serie($n) {
        for ($i=$n; $i > 0; $i--) {
            $tab[] = $i;
        }
        return $tab;
    }
    echo "n : ";
    $n = (int)readline("n : 1");
    $tab = serie($n);
    foreach($tab as $key=>$value) {
        echo $value." ";
    }
    echo "\n";