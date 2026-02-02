<?php
    function dPrime($nkid, $pay) {
        if (! ($nkid < 1)) {
            if (($nkid == 1 and $pay <= 33044) or ($nkid == 2 and $pay <= 38045) or ($nkid >= 3 and $pay <= 44046)) {
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return "error";
        }
    }
    $nkid = (int)readline("n of kids : ");
    $pay = (float)readline("money : ");
    echo dPrime($nkid, $pay)."\n";

?>