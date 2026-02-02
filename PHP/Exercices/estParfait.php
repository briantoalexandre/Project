<?php
    function Parf($n) {
        $k = 0;
        for($i=1; $i < $n; $i++) {
            $div = $n/$i;

            if ($div == intval($div)) {
                $k += $i;
            }
        }
        if ($k == $n){
            echo "$n is a perfect number";
            return true;
        }
        else {
            echo "$n is not a perfect number";
            return false;
        }
        
    }
    $n = readline("n : ");
    $val = Parf($n);
    echo "\n"
?>