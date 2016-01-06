<?php
	function startsWith($str, $check)
	{
	    return strpos($str, $check) === 0;
	}
	function endsWith($str, $check)
	{
	    return strpos($str, $check) + strlen($check) ===
	        strlen($str);
	}
?>