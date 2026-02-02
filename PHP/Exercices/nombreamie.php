<?php
    function nbFriend($n) {
        $tab = str_split(strval($n));
        $n1 = $tab[0];
        $k = 0;
        foreach($tab as $value) {
            if ($value != $n1) {
                return "False";
            }
        }
        return "True";
    }
    $n = (int)readline("n = ");
    $ans = nbFriend($n);
    echo "$ans\n";
