<?php
  ini_set('display_errors',1);
  error_reporting(E_ALL);
  require_once "pdo.php";
  session_start();

  $id = htmlentities($_GET['id']);

  if ( isset($_SESSION['error']) ) {
    echo '<p style="color:red">'.$_SESSION['error']."</p>\n";
    unset($_SESSION['error']);
  }


  if (isset($_POST['make']) && isset($_POST['model']) 
      && isset($_POST['year']) && isset($_POST['miles'])
      && isset($_POST['price'])
      && $_POST['make'] != "" && $_POST['model'] != ""
      && $_POST['year'] != "" && $_POST['miles'] != ""
      && $_POST['price'] != ""  ){

    $make = htmlentities($_POST['make']);
    $model = htmlentities($_POST['model']);
    $year = htmlentities($_POST['year']);
    $miles = htmlentities($_POST['miles']);
    $price = htmlentities($_POST['price']);

    if( is_numeric($year) && intval($year) > 0
        && is_numeric($miles) && intval($miles) > 0 
        && is_numeric($price) && intval($price) > 0  ){

      $sql = "UPDATE autos SET make = :make, model = :model, year = :year, 
              miles = :miles, price = :price WHERE id = :id";
      $stmt = $pdo->prepare($sql);
      $stmt->execute(array( 
          ':make' => $_POST['make'],
          ':model' => $_POST['model'], 
          ':year' => $_POST['year'],
          ':miles' => $_POST['miles'],
          ':price' => $_POST['price'], 
          ':id' => $id));
      $_SESSION['success'] = 'Record updated';
      header( 'Location: index.php' ) ;
      return;
    }
    else{
      $_SESSION['error']='Error in input data';
      header('Location: index.php') ;
      return;
    }

  }
  else{
      if( isset($_POST['btn']) && $_POST['btn'] == "Update" ){
      $_SESSION['error'] = 'All values are required';
      header('Location: index.php');
      return;
    }
  }

  $stmt = $pdo->prepare("SELECT * FROM autos where id = :xyz");
  $stmt->execute(array(":xyz" => $id));
  $row = $stmt->fetch(PDO::FETCH_ASSOC);
  if ( $row === false ) {
      $_SESSION['error'] = 'Bad value for id';
      header('Location: index.php') ;
      return;
  }

  $make = htmlentities($row['make']);
  $model = htmlentities($row['model']);
  $year = htmlentities($row['year']);
  $miles = htmlentities($row['miles']);
  $price = htmlentities($row['price']);

echo <<< _END
<p>Edit Record</p>
<form method="post">
<p>Make:
<input type="text" name="make" value="$make"></p>
<p>Model:
<input type="text" name="model" value="$model"></p>
<p>Year:
<input type="text" name="year" value="$year"></p>
<p>Miles:
<input type="text" name="miles" value="$miles"></p>
<p>Price:
<input type="text" name="price" value="$price"></p>
<input type="hidden" name="id" value="$id">
<p><input type="submit" name="btn" value="Update"/>
<a href="index.php">Cancel</a></p>
</form>
_END
?>

