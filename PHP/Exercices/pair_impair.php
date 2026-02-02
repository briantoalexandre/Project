<?php
    $n = (int)readline("n : ");
    if ($n%2==0) {
        echo("$n est pair\n");
    }
    else {
        echo("$n est impair\n");
    }
    for($i = $n; $i < $n+20; $i+=2 ) {
        echo "$i ";
    }
    echo "\n"
?>