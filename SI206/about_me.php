<?php
	session_start();
	$_SESSION['page']="about_me";
?>


<!DOCTYPE html>
<html lang="en">
<head>
	<?php
		include "meta.php";
		include "link.php";
		include "script.php";
	?>
	<title>Zijie Ku - About Me</title>
    <link rel="stylesheet" href="css/style-photo.css">
</head>
<body>
	<?php
		include "header.php";
	?>

	<hr class="style-hr">
	
	<article class="post">
		<header class="post-header">
			<h2 class="post-title"> Hello World?! o.O </h2>
		</header>
		<section class="post-excerpt">
			<h2> Intro </h2>
			<p>	I am Zijie. You can call me ZJ if you can't get the pronounciation right.<br>
				I am currently an undergraduate student in School of LSA, UofM. <br> 
				I am looking for a summer internship in cyber security.<br>
				Majors &amp; Minors</p>
			<ul>
				<li>Computer Science (Major)</li>
				<li>Statistics (Major)</li>
				<li>Mathematics (Minor) </li>
			</ul>
			<h2>Hobbies:</h2>
			<ul>
				<li>Cooking and Drinking (NOT an alcoholic)</li>
				<li>Shooting photos</li>
				<li>Improving cyber security knowledge</li>
			</ul>
			<h2>Skills: </h2>
			<ol>
				<li>Programming Skills
					<ul><li>Java, C, C++</li></ul>
				</li>

				<li>Web Development
					<ul><li>HTML, PHP, CSS, JavaScript</li></ul>
				</li>

				<li>Software
					<ul><li>Latex, Matlab and Mathematica</li></ul>
				</li>
			</ol>
			
			<p>Scan the QR code in this page to find out more about me.</p>
		</section>
		<footer class="post-meta">
			<time class="post-date" datetime="2014-12-16">
				2014-Dec-16
			</time>
		</footer>
	</article>

	<hr class="style-hr">

	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/qr-fb.png" alt="facebook qr code"
						class="img-responsive img-rounded" width="320">
					<figcaption> Facebook </figcaption>
				</figure>	
			</div>
		<!-- </div> -->

		<hr class="style-hr">

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/qr-wechat.jpg" alt="wechat qr code"
						class="img-responsive img-rounded" width="320">
					<figcaption> Wechat </figcaption>
				</figure>	
			</div>
		<!-- </div> -->

		<hr class="style-hr">

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/qr-this.png" alt="wechat qr code"
						class="img-responsive img-rounded" width="320">
					<figcaption> This website </figcaption>
				</figure>	
			</div>
		</div>
	</div>

	<hr class="style-hr">
	
	<?php
		include 'footer.php';
	?>

</body>
</html>