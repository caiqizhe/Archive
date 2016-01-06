<?php
  ini_set('display_errors',1);
  error_reporting(E_ALL);
  require_once "pdo.php";
  require_once 'helper_func.php';
  session_start();

  $id = htmlentities($_GET['id']);

  if ( isset($_SESSION['error']) ) {
    echo '<p style="color:red">'.$_SESSION['error']."</p>\n";
    unset($_SESSION['error']);
  }


  if ( isset($_POST['url']) && isset($_POST['email'])  
      && isset($_POST['length']) && isset($_POST['rating'])
      && $_POST['url'] != "" && $_POST['email'] != ""
      && $_POST['length'] != "" && $_POST['rating'] != "" ){

    $url = htmlentities($_POST['url']);
    $email = htmlentities($_POST['email']);
    $length = htmlentities($_POST['length']);
    $rating = htmlentities($_POST['rating']);

    if( ( startsWith($url,'http') || startsWith($url, 'https') )
        && (strpos($email, '@') !== FALSE)
        && is_numeric($length) && intval($length) > 0
        && is_numeric($rating) && intval($rating) > 0 ){

      $sql = "UPDATE videos SET url = :url, email = :email, length = :length, rating = :rating WHERE id = :id";
      $stmt = $pdo->prepare($sql);
      $stmt->execute(array( ':url' => $_POST['url'],
          ':email' => $_POST['email'], ':length' => $_POST['length'],
          ':rating' => $_POST['rating'], ':id' => $id));
      $_SESSION['success'] = 'Record updated';
      header( 'Location: index.php' ) ;
      return;
    }
    else{
      $_SESSION['error']='Error in input data';
      header('Location: edit.php?id='.$id) ;
      return;
    }

  }
  else{

      if( isset($_POST['btn']) && $_POST['btn'] == "Update" ){
        echo "yyy";
      $_SESSION['error'] = 'All values are required';
      header('Location: edit.php?id='.$id);
      return;
    }
  }

  $stmt = $pdo->prepare("SELECT * FROM videos where id = :xyz");
  $stmt->execute(array(":xyz" => $id));
  $row = $stmt->fetch(PDO::FETCH_ASSOC);
  if ( $row === false ) {
      $_SESSION['error'] = 'Bad value for id';
      header('Location: edit.php?id='.$id) ;
      return;
  }

  $u = htmlentities($row['url']);
  $e = htmlentities($row['email']);
  $l = htmlentities($row['length']);
  $r = htmlentities($row['rating']);

echo <<< _END
<p>Edit Record</p>
<form method="post">
<p>Url:
<input type="text" name="url" value="$u"></p>
<p>Email:
<input type="text" name="email" value="$e"></p>
<p>Length:
<input type="text" name="length" value="$l"></p>
<p>Rating:
<input type="text" name="rating" value="$r"></p>
<input type="hidden" name="id" value="$id">
<p><input type="submit" name="btn" value="Update"/>
<a href="index.php">Cancel</a></p>
</form>
_END
?>

