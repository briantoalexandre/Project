<?php
    for ($i = 0; $i < 10; $i++) {
        $tab[] = rand(1, 100);
    }
    foreach($tab as $index) {
        if ($index%2==0) {
            $tabP[] = $index;
        }
        else {
            $tabI[] = $index;
        }
    }
    echo "table : ";
    foreach($tab as $index) {
        echo $index." ";
    }
    echo "\nsum = ".array_sum($tab)."\nmin = ".min($tab)."\nmax = ".max($tab)."\n\n";
    echo "Even : ";
    foreach($tabP as $index) {
        echo $index." ";
    }
    echo "\nOdd : ";
    foreach($tabI as $index) {
        echo $index." ";
    }
    echo "\n";
?>