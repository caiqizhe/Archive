<?php
require_once "pdo.php";
ini_set('display_errors',1);
error_reporting(E_ALL);
session_start();

if ( isset($_SESSION['error']) ) {
    echo '<p style="color:red">'.$_SESSION['error']."</p>\n";
    unset($_SESSION['error']);
}


if( isset($_POST['make']) && isset($_POST['model']) 
  && isset($_POST['year']) && isset($_POST['miles'])
  && isset($_POST['price']) ){
    $sql = "INSERT INTO autos (make, model, year, miles, price) 
              VALUES (:make, :model, :year, :miles, :price)";

    $make = htmlentities($_POST['make']);
    $model = htmlentities($_POST['model']);
    $year = htmlentities($_POST['year']);
    $miles = htmlentities($_POST['miles']);
    $price = htmlentities($_POST['price']);

    if( is_numeric($year) && intval($year) > 0
      && is_numeric($miles) && intval($miles) > 0 
      && is_numeric($price) && intval($price) > 0 ){
      $stmt = $pdo->prepare($sql);
      $stmt->execute(array(
        ':make' => $make,
        ':model' => $model,
        ':year' => $year,
        ':miles' => $miles,
        ':price' => $price));
      $_SESSION['success'] = 'Record Added';
      header( 'Location: index.php' ) ;
      return;
    }
    else{
      $_SESSION['error'] = 'Error in input data';
      header( 'Location: index.php' ) ;
      return;
    }
}
else{
  if( isset($_POST['btn']) && $_POST['btn'] == "Add New" ){
    $_SESSION['error'] = 'All values are required';
    header( 'Location: index.php' ) ;
    return;
  }
}
?>
<p>Add A New Car</p>
<form method="post">
<p>Make:
<input type="text" name="make"></p>
<p>Model:
<input type="text" name="model"></p>
<p>Year:
<input type="text" name="year"></p>
<p>Miles:
<input type="text" name="miles"></p>
<p>Price:
<input type="text" name="price"></p>
<p><input type="submit" name="btn" value="Add New"/>
<a href="index.php">Cancel</a></p>
</form>

