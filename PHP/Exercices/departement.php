<?php
    $dep = array(75, 77, 78, 91, 92, 93, 94);
    #foreach($obj as $dep) {
    #    echo "$obj";
    #}
    do {
         $choix = (int)readline("\nchoisir un département : ");
    } while ($choix > 99 or $choix < 1);
    if (in_array($choix, $dep)) {
        echo "Le departement $choix est dans l'ile de France\n";
    }
    else {
        echo "Le departement $choix n'est pas dans l'ile de France\n";
    }
?>