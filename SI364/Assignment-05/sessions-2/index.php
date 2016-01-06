<?php
    session_start();
    if ( isset($_POST["street"]) && isset($_POST["city"]) &&
        isset($_POST["state"]) && isset($_POST["zip"]) ) {
        $_SESSION['street'] = $_POST['street'];
        $_SESSION['city'] = $_POST['city'];
        $_SESSION['state'] = $_POST['state'];
        $_SESSION['zip'] = $_POST['zip'];
        header( 'Location: index.php' ) ;
        return;
    }      
?>
<html>
<head>
</head>
<body style="font-family: sans-serif;">
<h1>Online Address Book</h1>
<?php 
    if ( isset($_SESSION["success"]) ) {
        echo('<p style="color:green">'.$_SESSION["success"]."</p>\n");
        unset($_SESSION["success"]);
    }  
 
    // Retrieve data form the session for the view
    $street = isset($_SESSION['street']) ? $_SESSION['street'] : '';
    $city = isset($_SESSION['city']) ? $_SESSION['city'] : '';
    $state = isset($_SESSION['state']) ? $_SESSION['state'] : '';   
    $zip = isset($_SESSION['zip']) ? $_SESSION['zip'] : '';  
 
    if ( ! isset($_SESSION["account"]) ) { 
?>


Please <a href="login.php">Log In</a> to start.
<?php } else { ?>
<p>Please enter your address:


<form method="post">
<p>Street: <input type="text" name="street" size="50" 
  value="<?php echo(htmlentities($street)); ?>"></p>
<p>City: <input type="text" name="city" size="20" 
  value="<?php echo(htmlentities($city)); ?>"></p>
<p>State: <input type="text" name="state" size="2" 
  value="<?php echo(htmlentities($state)); ?>">
Zip: <input type="text" name="zip" size="5" 
  value="<?php echo(htmlentities($zip)); ?>"></p>
<p><input type="submit" value="Update">
<input type="button" value="Logout"
  onclick="location.href='logout.php'; return false"></p>
</form>


<?php } ?>
</body>






