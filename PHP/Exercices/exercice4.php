<?php
    $sentence = readline("type a sentence : ");
    $size = strlen($sentence);
    if ($size > 10) {
        echo substr($sentence, 0, 10)."...\n";
    }
    else {
        echo $sentence."\n";
    }

?>
