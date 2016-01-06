<?php
	session_start();
	$_SESSION['page']="default";
?>


<!DOCTYPE html>
<html lang="en">
<head>	
	<?php
		include "meta.php";
		include "link.php";
		include "script.php";
	?>
	<title>Zijie Ku - Default</title>
</head>
<body>

	<?php
		include "header.php";
	?>

	<hr class="style-hr">

	<div id="wrapper">
		<div id="content">
			<h3>Awesome stuff requires your patience.</h3>
		</div>
	</div>

	<hr class="style-hr">

	<?php
		include 'footer.php';
	?>

</body>
</html>