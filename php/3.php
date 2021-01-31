<?php
$_sayi=$_POST["sayi"];
$sayac=0;
for($i=2; $i<$_sayi; $i++){
    if($_sayi%$i==0){
        $sayac=$sayac+1;
    }
}
if ($sayac != 0){
   echo("Girdiğiniz sayı asal değildir.");
}
else{
   echo("Girdiğiniz sayı asaldır.");
}
?>