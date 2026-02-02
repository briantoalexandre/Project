<?php
    function Oddsum($n) {
        $str_n = str_split(strval($n));
        $k = 0;
        foreach($str_n as $value) {
            $k += intval($value);
        }
        return $k;
    }
    
    $n = (int)readline("n = ");
    $answer = Oddsum($n);
    echo "$answer\n";

