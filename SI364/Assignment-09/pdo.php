<?php
  ini_set('display_errors',1);
  error_reporting(E_ALL);
  try{
    define('DB_HOST', getenv('OPENSHIFT_MYSQL_DB_HOST'));
    define('DB_PORT',getenv('OPENSHIFT_MYSQL_DB_PORT')); 
    define('DB_USER',getenv('OPENSHIFT_MYSQL_DB_USERNAME'));
    define('DB_PASS',getenv('OPENSHIFT_MYSQL_DB_PASSWORD'));
    define('DB_NAME',getenv('OPENSHIFT_GEAR_NAME'));
  	$dsn = 'mysql:dbname='.DB_NAME.';host='.DB_HOST.';port='.DB_PORT;
  	// echo $dsn;
    $pdo = new PDO($dsn, 'user', 'ZRrLA2HmuJxSs5GG');
  } catch(Exception $ex){
  	die($ex->getMessage());
  }
  // var_dump($pdo)
?>
