<?php
  ini_set('display_errors',1);
  error_reporting(E_ALL);
  require_once "pdo.php";
?>
<html>
<head>
  <title>Zijie Ku</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<?php
  $query = 'SELECT S.sName AS sName, S.sID AS sID, 
              C.cName AS cName, A.major AS major
            FROM College C, Student S, Apply A
            WHERE C.cName = A.cName
            AND S.sID = A.sID';

  if( isset( $_GET['method']) ){
    $choice = $_GET['method'];
    switch( $choice ){
      case 'sName':
          $query = $query.' '.'ORDER BY sName';
      break;
      case 'sID':
          $query = $query.' '.'ORDER BY sID';
      break;
      case 'cName':
          $query = $query.' '.'ORDER BY cName';
      break;
      case 'major':
          $query = $query.' '.'ORDER BY major';
      break;
      default:
          echo "wrong";
      break;
    }
  }
  else{
    $query = $query.' '.'ORDER BY S.sName';
  }
  $stmt = $pdo->query($query);
  echo('<table border="1">'."\n");
  
  echo('<form id="form" method="GET">');
  
  echo("<tr><th>");

  echo('<a href="index.php">');
  echo("Student Name</a>");
  echo("</th><th>");

  echo('<a href="index.php?method=sID">');
  echo("Student ID</a>");
  echo("</th><th>");

  echo('<a href="index.php?method=cName">');
  echo("College Name</a>");
  echo("</th><th>");

  echo('<a href="index.php?method=major">');
  echo("Major</a>");
  echo("</th></tr>");

  echo('</form>');

  while ( $row = $stmt->fetch(PDO::FETCH_ASSOC) ) {
    echo('<tr><td class="sName">');
    echo($row['sName']);
    echo('</td><td class="sID">');
    echo($row['sID']);
    echo('</td><td class="cName">');
    echo($row['cName']);
    echo('</td><td class="major">');
    echo($row['major']);
    echo("</td></tr>\n");
  }

  echo('</table>');
?>
</body>
</html>
