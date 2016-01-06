<?php
ini_set('display_errors',1);
error_reporting(E_ALL);
require_once "pdo.php";
require_once 'helper_func.php';
session_start();

$id = htmlentities($_GET['id']);
if ( isset($_POST['delete']) && isset($_POST['id']) ) {
    $sql = "DELETE FROM videos WHERE id = :zip";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(array(':zip' => $id));
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    $_SESSION['success'] = 'Record deleted';
    header( 'Location: index.php' ) ;
    return;
}

$stmt = $pdo->prepare("SELECT url, id FROM videos where id = :xyz");
$stmt->execute(array(":xyz" => $id));
$row = $stmt->fetch(PDO::FETCH_ASSOC);
if ( $row === false ) {
    $_SESSION['error'] = 'Bad value for id';
    header( 'Location: index.php' ) ;
    return;
}

echo "<p>Confirm: Deleting ".$row['url']."</p>\n";
echo('<form method="post"><input type="hidden" ');
echo('name="id" value="'.$id.'">'."\n");
echo('<input type="submit" value="Delete" name="delete">');
echo('<a href="index.php">Cancel</a>');
echo("\n</form>\n");
?>