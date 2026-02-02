<?php
    function Prem($n) {
        $lim = (int)sqrt($n);
        echo "$lim\n";
        for($i=2; $i < $lim; $i++) {
            $div = $n/$i;
            if ($div == intval($div)) {
                return "$n n'est pas un nombre premier";
            }
        return "$n est un nombre premier";
        }
        
    }
    $n = readline("n : ");
    $val = Prem($n);
    echo $val;