<?php
    $cont = ["Fr"=>5, "US"=>6, "EU"=>7, "De"=>8];
    foreach($cont as $key => $value) {
        if ($value > 6) {
            echo $key."\n";
        }

    }