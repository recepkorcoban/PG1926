<?php
date_default_timezone_set('Europe/Istanbul');

$saat = date("G");
echo "SAAT: $saat<br>";
$intsaat=intval($saat);

if($intsaat>6 and $intsaat < 10){
    echo "Günaydın";
}
elseif($intsaat>10 and $intsaat<17){
    echo "İyi Günler";
}
elseif($intsaat>17 and $intsaat<20){
    echo "İyi akşamlar";
}
elseif($intsaat>20 and $intsaat<0){
    echo "İyi geceler";
}
elseif($intsaat>0 and $intsaat<6){
   echo "Esenlikler dilerim";
}

?>