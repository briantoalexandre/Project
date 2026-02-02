<?php
    $name = readline("name : ");
    $sname = readline("second name : ");
    echo strtoupper($sname)." (".strlen($sname).") ". ucwords(strtolower($name))." (".strlen($name).")\n";
?>