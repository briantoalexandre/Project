<?php
    $annee = (int)readline("Choisir une année : ");
    if (($annee %4==0 and ! $annee%100==0) or $annee%400==0) {
        echo "l'annee $annee est bissextile\n";
    }
    else {
        echo "l'annee $annee n'est pas bissextile\n";
    }
?>