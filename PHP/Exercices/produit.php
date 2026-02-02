<?php
    $n1 = (int)readline("n1 : ");
    $n2 = (int)readline("n2 : ");
    echo "chiffre 1 --> $n1, chiffre 2 --> ----- produit ";
    if ($n1 > 0) {
        if ($n2 > 0){
                echo "positif\n";
        }
        else {
            echo "négatif\n";
        }
    }
    else {
        if ($n2 > 0){
                echo "négatif\n";
        }
        else {
            echo "positif\n";
        }
    }
?>