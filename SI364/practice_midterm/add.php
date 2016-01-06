<?php
require_once 'helper_func.php';
require_once "pdo.php";
ini_set('display_errors',1);
error_reporting(E_ALL);
session_start();

if ( isset($_SESSION['error']) ) {
    echo '<p style="color:red">'.$_SESSION['error']."</p>\n";
    unset($_SESSION['error']);
}

if ( isset($_POST['url']) && isset($_POST['email']) 
  && isset($_POST['length']) && isset($_POST['rating'])
  && $_POST['url'] != "" && $_POST['email'] != ""
  && $_POST['length'] != "" && $_POST['rating'] != "") {
    $sql = "INSERT INTO videos (url, email, length, rating) 
              VALUES (:url, :email, :length, :rating)";
    
    $url = htmlentities($_POST['url']);
    $email = htmlentities($_POST['email']);
    $length = htmlentities($_POST['length']);
    $rating = htmlentities($_POST['rating']);
    if( ( startsWith($url,'http') || startsWith($url, 'https') )
      && (strpos($email, '@') !== FALSE)
      && is_numeric($length) && intval($length) > 0
      && is_numeric($rating) && intval($rating) > 0 ){
      $stmt = $pdo->prepare($sql);
      $stmt->execute(array(
        ':url' => $url,
        ':email' => $email,
        ':length' => $length,
        ':rating' => $rating));
      $_SESSION['success'] = 'Record Added';
      header( 'Location: index.php' ) ;
      return;
    }
    else{
      $_SESSION['error'] = 'Error in input data';
      header( 'Location: add.php' ) ;
      return;
    }
}
else{
  if( isset($_POST['btn']) && $_POST['btn'] == "Add New" ){
    $_SESSION['error'] = 'All values are required';
    header( 'Location: add.php' ) ;
    return;
  }
}
?>
<p>Add A New Record</p>
<form method="post">
<p>Url:
<input type="text" name="url"></p>
<p>Email:
<input type="text" name="email"></p>
<p>Length:
<input type="text" name="length"></p>
<p>Rating:
<input type="text" name="rating"></p>
<p><input type="submit" name="btn" value="Add New"/>
<a href="index.php">Cancel</a></p>
</form>

