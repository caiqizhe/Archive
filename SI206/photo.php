<?php
	session_start();
	$_SESSION['page']="photo";
?>


<!DOCTYPE html>
<html lang="en">
<head>
	<?php
		include "meta.php";
		include "link.php";
		include "script.php";
	?>
	<title>Zijie Ku - Photo</title>
    <link rel="stylesheet" href="css/style-photo.css">
</head>
<body>
	<?php
		include "header.php";
	?>
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-12.jpg" alt="Ball 8"
						class="img-responsive img-rounded">
					<figcaption> Ball 8 </figcaption>
				</figure>	
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-01.jpg" alt="game-time"
						class="img-responsive img-rounded">
					<figcaption> Pool Time</figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-02.jpg" alt="drink-time"
						class="img-responsive img-rounded">
					<figcaption> Whiskey </figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-03.jpg" alt="rest-time" 
						class="img-responsive img-rounded">
					<figcaption> I Love Canadian Ice Wine </figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-11.jpg" alt="Music" 
						class="img-responsive img-rounded">
					<figcaption> Music is life </figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-05.jpg" alt="Rain" 
						class="img-responsive img-rounded">
					<figcaption> Moody </figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-06.jpg" alt="Dumplings" 
						class="img-responsive img-rounded">
					<figcaption> Dumplings </figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-07.jpg" alt="Buddha" 
						class="img-responsive img-rounded">
					<figcaption> Buddha </figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-08.jpg" alt="Monkey eating chips" 
						class="img-responsive img-rounded">
					<figcaption> Classic Flavor? </figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-09.jpg" alt="xxoo" 
						class="img-responsive img-rounded">
					<figcaption> Spring </figcaption>
				</figure>
			</div>
		<!-- </div> -->
		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-10.jpg" alt="naughty monkey" 
						class="img-responsive img-rounded">
					<figcaption> Naughty </figcaption>
				</figure>
			</div>
		<!-- </div> -->

		<!-- <div class="row"> -->
			<div class="col-lg-4 col-sm-6 col-xs-12">
				<figure>
					<img src="./img/sample-04.jpg" alt="Favorite-drink" 
						class="img-responsive img-rounded">
					<figcaption> Ginger Honey Wine </figcaption>
				</figure>
			</div>
		</div>
	</div>

	<?php
		include 'footer.php';
	?>
</body>
</html>