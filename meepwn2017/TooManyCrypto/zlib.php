<?php
	$c = "secret=";
	echo bin2hex(gzcompress($c,-1));
?>
