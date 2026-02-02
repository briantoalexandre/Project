<?php
    function range1($n) {
        for ($i=1; $i <= $n; $i++) {
            $tab[] = $i;
        }
        return $tab;
    }
    function pair($tab) {
        foreach($tab as $value) {
            if ($value%2==0) {
                $table[] = $value;
            }
        }
        return $table;
    }
    function impair($tab) {
        foreach($tab as $value) {
            if ($value%2!=0) {
                $table[] = $value;
            }
        }
        return $table;
    }
    function parite($tab) {
        $assoc = ["pair" => [], "impair" => []];
        foreach($tab as $value) {
            if ($value % 2 == 0) {
                $assoc["pair"][] = $value;}
            else {
                $assoc["impair"][] = $value;
            }
        }
        return $assoc;
    }

    $n = readline("n : 1");
    $tab = range1($n);

    $tpair = pair($tab);
    $timpair = impair($tab);
    $seg = parite($tab);

    foreach($seg as $key=>$value) {
        echo "\n$key : ";
        foreach($value as $i) {
            echo "$i ";
        }
        echo "\n";
    }

    /*
    echo "pair : ";
    foreach($tpair as $value) {
        echo "$value ";
    }
    echo "\nimpaire : ";
    foreach($timpair as $value) {
        echo "$value ";
    }*/

    echo "\n";