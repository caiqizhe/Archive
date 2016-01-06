<?php
	session_start();
?> 
	<!-- Nav bar is taken from http://getbootstrap.com/components/#navbar -->
	<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
		<div class="container-fluid">
	    <!-- Brand and toggle get grouped for better mobile display -->
	    <div class="navbar-header">
	    	<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" 
	    		data-target="#bs-example-navbar-collapse-1">
		        <span class="sr-only">Toggle navigation</span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="http://si206-kuzijie.rhcloud.com/">
				Z.K | Zijie Ku
			</a>
	    </div>

		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
			<li id="home" class=""><a href="index.php">
				<span class="glyphicon glyphicon-home"></span> Home </a></li>
			<li id="photo" class=""><a href="photo.php">
				<span class="glyphicon glyphicon-camera"></span> Photos </a></li>
			<li id="coding" class="dropdown">
				<a href="photo.php" class="dropdown-toggle" data-toggle="dropdown">
					<span class="glyphicon glyphicon-thumbs-up"></span> Codings
					<span class="caret"></span></a>
				<ul class="dropdown-menu" role="menu">
					<li><a href="https://github.com/zijieku/si206">
						<span class="glyphicon glyphicon-link"></span> SI206 </a>
					</li>

					<li><a href="https://github.com/zijieku/si364">
						<span class="glyphicon glyphicon-link"></span> SI364 </a>
					</li>
					
					<li class="divider"></li>
					<li><a href="default.php">
						<span class="glyphicon glyphicon-pushpin"></span> Java </a>
					</li>
					<li><a href="default.php">
						<span class="glyphicon glyphicon-pushpin"></span> C++ </a>
					</li>
					<li class="divider"></li>
					<li><a href="default.php">
						<span class="glyphicon glyphicon-globe"></span> PHP </a>
					</li>
					<li><a href="default.php">
						<span class="glyphicon glyphicon-globe"></span> Database </a>
					</li>
				</ul>
			</li>
		  </ul>

	      <ul class="nav navbar-nav navbar-right">
	        <li id="about_me"><a href="about_me.php">
	        	<span class="glyphicon glyphicon-qrcode"></span> About Me </a>
	        </li>
	        <li id="contact"><a href="contact.php">
	        	<span class="glyphicon glyphicon-send"></span> Contact </a>
	        </li>
	      </ul>
	    </div><!-- /.navbar-collapse -->
	  </div><!-- /.container-fluid -->
	</nav>

	<?php
		$background_img = "background-01.jpg";
		if( $_SESSION['page'] == 'index' ){
			$background_img = "background-03.jpg";
		}
		else if( $_SESSION['page'] == 'about_me' ){
			$background_img = "background-00.jpg";
		}
		else if( $_SESSION['page'] == 'default' ){
			$background_img = "background-01.jpg";

		}
		else if( $_SESSION['page'] == 'photo' ){
			$background_img = "background-02.jpg";
		}
		echo ('<header class="main-header" '.
			'style="background-image: url(http://si206-kuzijie.rhcloud.com/img/'.
			$background_img.');">');
	?>

	
	<div class="vertical">
	    <div class="main-header-content inner">
	        <h1 class="page-title">Code-Monkey</h1>
	        <h2 class="page-description">My final portfolio.</h2>
	    </div>
	</div>
	</header>


<!-- 	<div id="social">
      <ul>
        <li><a href="https://www.facebook.com/public/Ku-Zijie"><img src="./img/facebook.png" alt="facebook link" height="25" width="25"/></a></li>
        <li><a href="http://instagram.com/zijieku/"><img src="./img/instagram.jpg" alt="instagram link" height="25" width="25"/></a></li>
      </ul>
	</div>
 -->

	<div class="sticky-container">
		<ul class="sticky">
			<li>
				<a href="http://instagram.com/zijieku/">
					<img width="32" height="32" title="instagram" alt="instagram link" src="./img/instagram.png">
					<p>Instagram</p>
				</a>
			</li>
			<li>
				<a href="https://www.facebook.com/ku.zijie">
					<img width="32" height="32" title="facebook" alt="facebook link" src="./img/facebook.png">
					<p>Facebook</p>
				</a>
			</li>

		</ul>
	</div>

<?php
	$title = "<title>Zijie Ku - ";
	
	if( $_SESSION['page'] == 'index' ){
		// echo ($title."home</title>");
		echo ("<script>");
		echo ("var element = document.getElementById('home');");
	}
	else if( $_SESSION['page'] == 'about_me' ){
		// echo ($title."About Me</title>");
		echo ("<script>");
		echo ("var element = document.getElementById('about_me');");
	}
	else if( $_SESSION['page'] == 'default' ){
		// echo ($title."default</title>");
		echo ("<script>");
		echo ("var element = document.getElementById('coding');");
	}
	else if( $_SESSION['page'] == 'photo' ){
		// echo ($title."photo</title>");
		echo ("<script>");
		echo ("var element = document.getElementById('photo');");
	}
	else if( $_SESSION['page'] == 'contact' ){
		// echo ($title."photo</title>");
		echo ("<script>");
		echo ("var element = document.getElementById('contact');");
	}
	echo ("element.classList.add('active');");
	echo ("</script>");
?>

