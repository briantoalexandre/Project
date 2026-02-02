<?php
    $age = (int)readline("age : ");
    if (26 < $age and $age <= 65) {
        echo "Tarif pas réduit\n";
    }
    else {
        echo "Tarif réduit, bravo!\n";
    }
?>