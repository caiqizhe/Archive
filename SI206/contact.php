<?php
	session_start();
	$_SESSION['page']="contact";
?>

<!DOCTYPE html>
<html lang="en">
<head>
	<?php
		include "meta.php";
		include "link.php";
		include "script.php";
	?>
	<title>Zijie Ku - Contact</title>
    <link rel="stylesheet" href="css/style-photo.css">
</head>
<body>
	<?php
		include "header.php";
	?>

  <?php
  if( isset($_SESSION['email_status']) ){ 
    if($_SESSION['email_status'] == "sent" ){
      echo('<div class="alert alert-success" role="alert">');
          echo('<span class="glyphicon glyphicon-ok-circle"></span>');
          echo('<a href="#" class="close" data-dismiss="alert">&times;</a>');
          echo('<strong>Success! </strong> email sent.');
        echo('</div>');
          unset($_SESSION['email_status']);
    }
    else{
      echo('<div class="alert alert-danger" role="alert">');
          echo('<span class="glyphicon glyphicon-exclamation-sign"></span>');
          echo('<a href="#" class="close" data-dismiss="alert">&times;</a>');
          echo('<strong>Error! </strong>'." error sending email.");
          echo('</div>');
          unset($_SESSION['email_status']);
    }
      
    }
  ?>

	<div class="container">
    <h2>Contact Me</h2>
    <form role="form" action="email.php" method="POST">
      <div class="form-group">
        <label for="sender_email">Email:</label>
        <input type="email" class="form-control" name="sender_email" id="sender_email" placeholder="Enter email" required>
      </div>
      <div class="form-group">
        <label for="sender_name">Name:</label>
        <input type="text" class="form-control" name="sender_name" id="sender_name" placeholder="Enter name" required>
      </div>
      <div class="form-group">
        <label for="message">Message:</label>
        <textarea class="form-control"  rows="5" name="message" id="message" placeholder="Enter message" required></textarea>
      </div>
      <button type="submit" class="btn btn-default">Submit</button>
    </form>
  </div>

	
	<?php
		include 'footer.php';
	?>

</body>
</html>