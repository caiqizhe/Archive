<?php
	session_start();
	$last_modified = "";
	if( $_SESSION['page'] == 'index' ){
		$last_modified = filemtime("index.php");
	}
	else if( $_SESSION['page'] == 'about_me' ){
		$last_modified = filemtime("about_me.php");
	}
	else if( $_SESSION['page'] == 'default' ){
		$last_modified = filemtime("default.php");
	}
	else if( $_SESSION['page'] == 'photo' ){
		$last_modified = filemtime("photo.php");
	}
	else if( $_SESSION['page'] == 'contact' ){
		$last_modified = filemtime("contact.php");
	}
?>

<?php

	echo ('<footer class="modified-meta">');
	// echo ('<time>');
	echo ("Last modified: ".date("F d Y H:i:s.", $last_modified));
	// echo ('</time>');
	echo ('</footer>');

	echo( '<footer class="site-footer">' );
	echo( '<section class="copyright">' );
	echo( '<a href="http://si206-kuzijie.rhcloud.com/">' );
	echo( '<h6>Zijie Ku - Code Monkey &copy;</h6>' );
	echo( '</a>' );
	echo( '<h6>All photos &copy; 2000-2014 Zijie Ku</h6>' );
	echo( '</section>' );
	echo( '<section class="motto">' );
	echo( '<h6>Simplicity is the ultimate sophistication</h6>');
	echo( '</section>' );
	echo( '</footer>' );
?>