<?php
    session_start();
    if ( isset($_POST["sugar"]) && isset($_POST["spice"]) &&
        isset($_POST["vanilla"]) ) {
        $_SESSION['sugar'] = $_POST['sugar'];
        $_SESSION['spice'] = $_POST['spice'];
        $_SESSION['vanilla'] = $_POST['vanilla'];
        header( 'Location: index.php' ) ;
        return;
    } 
?>

<html>
	<head>
		<title>This Shopping Cart is From Zijie Ku</title>
	</head>

	<body style="font-family: sans-serif;">
		<h1>Welcome to Yarra Shopping Network</h1>

		<?php
			if ( isset($_SESSION["success"]) ) {
       			 echo('<p style="color:green">'.$_SESSION["success"]."</p>\n");
        		 unset($_SESSION["success"]);
    		}  

    		$sugar = isset($_SESSION['sugar']) ? $_SESSION['sugar'] : '';
    		$spice = isset($_SESSION['spice']) ? $_SESSION['spice'] : '';
    		$vanilla = isset($_SESSION['vanilla']) ? $_SESSION['vanilla'] : '';

    		if( !isset($_SESSION["account"]) ) { ?>	

    		Please <a href="login.php">Log In</a> to start.
    	<?php } else { ?>
    			<p>Please indicate how many of the following items you would like to purchase:</p>
    			<form method="post">
    			<p><input type="text" name="sugar" size="3" 
    				value="<?php echo(htmlentities($sugar)); ?>"> Sugar 4.50</p>
    			<p><input type="text" name="spice" size="3" 
    			value="<?php echo(htmlentities($spice)); ?>"> Spice 2.25</p>
    			<p><input type="text" name="vanilla" size="3" 
    				value="<?php echo(htmlentities($vanilla)); ?>"> Vanilla 3.35</p>
                <p><b>Order total: 
                    <?php
                        echo ($sugar * 4.5 + $spice * 2.25 + $vanilla * 3.35);
                    ?>
                    </b></p>
    			<input type="submit" value="Update">
                <input type="submit" value="Logout"
                        onclick="location.href='logout.php';return false">
    			<p>Many people who purchased both the first item and the second item were very nice</p>

    			<a href="logout.php">Logout</a>
    		</form>
    		<?php } ?>
	</body>
</html>


