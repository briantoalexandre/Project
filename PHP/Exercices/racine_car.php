<?php
    try {
        $n1 = (float)readline("a : ");
        $n2 = (float)readline("b : ");
        echo "La racine carré de a et b est ".sqrt($n1/$n2)."\n";
    }
    catch (DivisionByZeroError) {
        echo "Pas de division par Zero\n";
    } 
?>