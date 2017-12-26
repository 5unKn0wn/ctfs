<?php
	function tsu_super_encrypt0($c) {
		return gzcompress($c,-1);
	}

	function tsu_super_encrypt1($c,$key) {
		$l=strlen($key);
		$string="";
		for($i=0;$i<strlen($c);$i++) {
			$string[$i]=chr((ord($c[$i]) | ord($key[$i%$l])) & (256+~(ord($c[$i]) & ord($key[$i%$l])))%256);
		}
		return implode("",$string);
	}

	function tsu_super_encrypt2($c) {
		$l=strlen($c);
		$string="";
		for($i=0;$i<$l;$i++) {
			$string[$i]=chr((ord($c[$i])+$i)%256);
		}
		return implode("",$string);
	}

	function tsu_super_encrypt3($c) {
		$l=strlen($c);
		$k=$l%8;
		$string="";
		for($i=0;$i<$l;$i++) {
			$string[$i]=chr(((ord($c[$i])<<$k)|ord($c[$i])>>(8-$k))&0xff);
		}
		return implode("",$string);
	}	

	$enc = "1234567890qwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewq0987654321";
	$flag = "salt";
	$query = "secret=" . $flag . "string=" . $enc;
	$key = "key";
	$encrypted0=tsu_super_encrypt0($query);
	$encrypted1=tsu_super_encrypt1($encrypted0,$key);
	$encrypted2=tsu_super_encrypt2($encrypted1);
	$encrypted3=tsu_super_encrypt3($encrypted2);

	echo base64_encode($encrypted3);
?>
