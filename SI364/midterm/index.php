<?php
  ini_set('display_errors',1);
  error_reporting(E_ALL);
  require_once "pdo.php";
  session_start();
?>
<html>
<head>
  <title>Zijie Ku</title>
</head>


<body>
<?php
  if ( isset($_SESSION['error']) ) {
      echo '<p style="color:red">'.$_SESSION['error']."</p>\n";
      unset($_SESSION['error']);
  }
  if ( isset($_SESSION['success']) ) {
      echo '<p style="color:green">'.$_SESSION['success']."</p>\n";
      unset($_SESSION['success']);
  }
  echo('<table border="1">'."\n");
  $stmt = $pdo->query("SELECT id, make, model, year, miles, price FROM autos");
  while ( $row = $stmt->fetch(PDO::FETCH_ASSOC) ) {
      $id = htmlentities($row['id']);
      echo "<tr><td>";
      echo($row['make']);
      echo("</td><td>");
      echo($row['model']);
      echo("</td><td>");
      echo($row['year']);
      echo("</td><td>");
      echo($row['miles']);
      echo("</td><td>");
      echo($row['price']);
      echo("</td><td>");
      echo('<a href="edit.php?id='.$id.'">Edit</a> /');
      echo('<a href="delete.php?id='.$id.'">Delete</a>');
      echo("</td></tr>\n");
  }
?>
</table>
<a href="add.php">Add New</a>
</body>
</html>
