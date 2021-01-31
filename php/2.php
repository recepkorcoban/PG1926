<?php
$_sayi=$_POST["sayi"];
$toplam = 0;
for($i=1; $i < $_sayi; $i++){
    if($_sayi % $i==0){
        $toplam=$toplam+$i;
    }
}
if ($toplam == $_sayi) 
{ 
   echo ("$_sayi sayısı Mükemmel Sayıdır"); 
}
else 
{ 
   echo ("$_sayi sayısı Mükemmel Sayı Değildir"); 
} 


?>