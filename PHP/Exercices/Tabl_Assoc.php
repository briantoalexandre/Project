<?php
    $tab = ["a"=>[1, 2, 3], "b"=>[2, 3, 4], "c"=>[3,4,5], "d"=>[6,7,8], "e"=>[9,10,11]];
    foreach($tab as $key=>$value) {
        $avePer = 0;
        $ave = [];
        $nCount = count($value);
        echo $key." : ";
        foreach($value as $i) {
            echo $i." ";
            $avePer += $i; #$ave for average
            $ave[] = $i;
        }
        echo "\nAverage : ".($avePer/$nCount)."\n\n";

    }
    echo "\nAverage of the class : ".(array_sum($ave)/count($ave))."\n";