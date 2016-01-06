<?php
  ini_set('display_errors',1);
  error_reporting(E_ALL);
  require_once "pdo.php";
  session_start();

  $id = htmlentities($_GET['id']);
  if ( isset($_POST['title']) && isset($_POST['plays']) 
       && isset($_POST['rating']) && isset($_POST['id']) ) {
      $sql = "UPDATE tracks SET title = :title, 
              plays = :plays, rating = :rating
              WHERE id = :id";
      
      $stmt = $pdo->prepare($sql);
      $stmt->execute(array(
          ':title' => $_POST['title'],
          ':plays' => $_POST['plays'],
          ':rating' => $_POST['rating'],
          ':id' => $id));
      $_SESSION['success'] = 'Record updated';
      header( 'Location: index.php' ) ;
      return;
  }

$stmt = $pdo->prepare("SELECT * FROM tracks where id = :xyz");
$stmt->execute(array(":xyz" => $id));
$row = $stmt->fetch(PDO::FETCH_ASSOC);
if ( $row === false ) {
    $_SESSION['error'] = 'Bad value for id';
    header( 'Location: index.php' ) ;
    return;
}

$n = htmlentities($row['title']);
$e = htmlentities($row['plays']);
$p = htmlentities($row['rating']);

echo <<< _END
<p>Edit Record</p>
<form method="post">
<p>Title:
<input type="text" name="title" value="$n"></p>
<p>Plays:
<input type="text" name="plays" value="$e"></p>
<p>Rating:
<input type="text" name="rating" value="$p"></p>
<input type="hidden" name="id" value="$id">
<p><input type="submit" value="Update"/>
<a href="index.php">Cancel</a></p>
</form>
_END
?>

