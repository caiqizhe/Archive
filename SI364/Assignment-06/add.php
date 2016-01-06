<?php
require_once "pdo.php";
ini_set('display_errors',1);
error_reporting(E_ALL);
session_start();

if ( isset($_POST['title']) && isset($_POST['plays']) 
     && isset($_POST['rating'])) {
    $sql = "INSERT INTO tracks (title, plays, rating) 
              VALUES (:title, :plays, :rating)";
    
    $title = htmlentities($_POST['title']);
    $plays = htmlentities($_POST['plays']);
    $rating = htmlentities($_POST['rating']);

    if( is_numeric($plays) && is_numeric($rating) ){
      $stmt = $pdo->prepare($sql);
      $stmt->execute(array(
        ':title' => $title,
        ':plays' => $plays,
        ':rating' => $rating));
      $_SESSION['success'] = 'Record Added';
      header( 'Location: index.php' ) ;
      return;
    }
    else{
      $_SESSION['error'] = 'Bad value for title, plays, or rating';
      header( 'Location: index.php' ) ;
      return;
    }
}
?>
<p>Add A New Record</p>
<form method="post">
<p>Title:
<input type="text" name="title"></p>
<p>Plays:
<input type="text" name="plays"></p>
<p>Rating:
<input type="text" name="rating"></p>
<p><input type="submit" value="Add New"/>
<a href="index.php">Cancel</a></p>
</form>

