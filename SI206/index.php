<?php
	session_start();
	$_SESSION['page']="index";
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <?php
		include "meta.php";
		include "link.php";
		include "script.php";
	?>
	<title>Zijie Ku - Home</title>
</head>
<body>


	<?php
		include "header.php";
	?>
	<div class="container"> 
		<div class="row"> 

		<hr class="style-hr">
		<article class="post">
			<div id="post-header-2" class="post-header">
				<h2 class="post-title"> SI206 Final Personal Portfolio</h2>
			</div>
			<section class="post-excerpt">
				<h2>Checklists:</h2>
				<p> <b>Requirement:</b> <br>
					Portfolio must be at least three(3) pages and use PHP.<br>
					<b>Fullfillment:</b> <br>
					There're total five(5) pages created using php 
				</p>
				<ul>
					<li>index.php [Home]</li>
					<li>photo.php [Photo]</li>
					<li>about_me.php [About Me]</li>
					<li>contact.php [contact]</li>
					<li>default.php</li>
				</ul>
				<p>	
					All links in the navigation bar have been tested.
					There are links to external sources such as github.<br>
					The source code of this page is available online.
					Please free to copy, modify and redistribute.<br>
				</p>
				<ol>
					<li>
						<b>Requirement for Header:</b> <br>
						"The header must be nicely styled and interesting. Use an image, logo, gradient, something other than plain text."<br>
						<b>Fullfillment:</b> <br>
						Navigation bar is included in the header.php.<br>
						I hope the navigation bar is considered as "nicely styled".<br>
						At least according to my taste, it's decent. =)
					</li>

					<li>
						<b>Requirement for Navigation bar:</b> <br>
						"The navigation bar can be located anywhere you would like (absolute, fixed, top, side, a mixture based on viewport)."<br>
						<b>Fullfillment:</b> <br>
						Yes, trust me! It's in the right place!
					</li>
					<li>
						<b>Requirement for Footer:</b> <br>
						"The footer must be nicely styled and interesting."<br>
						<b>Fullfillment:</b> <br>
						Please see part 1. (saving dozens of words here...) &gt;.&lt;
					</li>
					<li>
						<b>Requirement for Content:</b> <br>
						The content is completely up to you. But each content page must include a minimum of <span style="color:red">two</span> paragraphs or some other original 
						content that takes up a majority of the window. <br>
						I will grade on spelling, grammar, etc. <span style="color:red">At least two of the three pages must</span> 
						have text. One page must have <span style="color:red">a working form</span> that is integrated nicely into your site. (So don’t just spit out the form data.)<br>
						<b>Fullfillment:</b> <br>
						Since the content is up to me, I have no idea what to write about.<br>
						I will just write a checklist. It should make it easier for grading.<br>
						The index.php and about_me.php are the two pages with text.<br>
						All posts I have made sits nicely within the article tags.<br>
						I will add a working form to about me page. I only notice that when I'm working on this checklist. OMG!<br>
						Please! Do NOT comment on my English! That's not my native language.
					</li>
					<li>
					  <b>Other Requirements:</b> <br>
					  <ul>
					  <li>You must use a fluid design and have at least three different views.</li>
					  <li>You should follow the general guidelines discussed in class. If you take particular pains to address accessibility, tell me.</li>
					  <li>Pages do not need to completely validate, as long as the errors are caused by code completely outside of your control.</li>
					  </ul>
					  <b>Fullfillment:</b> <br>
					  <p>Well, I am pretty sure my site is responsive and have been validated agaist the <a href="http://validator.w3.org">w3 html5 validator</a>.<br>
					  The site also passes <a href="http://wave.webaim.org">WAVE Accessibility</a> tests, although it comes with a couple of warnings, not errors. I guess they are OK.</p>
					</li>
					<li>
						<b>Requirements for Submission:</b> <br>
						<ol>
						<li>Where you used PHP?</li>
						<li>What grade you expect to receive?</li>
						<li>Why you expect to get that grade. (Assume an extra 2% for each "interesting" addition.)?</li>
						</ol>
						<b>Fullfillment:</b> <br>
						I used PHP as a template for header and footer.<br>
						Grades? Shhhhh... I will put that under the comments section on Ctools.<br>
						Additional stuff? Hmmmm... I added new social media links floating on the right-hand side (precisely 130 pixels counting from top). <br>
						Asians like Math and they like to be precised about everything! Yep! I like sarcasm! No hard feelings though.<br>
						Watch the video below to get my sense of humor! AND I'm NOT KOREAN!<br>
						Also, I embeded a video in this page.
					</li>        
				</ol>
			</section>
			<div class="col-sm-12">
            	<iframe class="col-xs-12" height="320" src="//www.youtube.com/embed/CrI64F2Xzxw" style="border:0;" allowfullscreen></iframe>
        	</div>
			<br>
			<br>
			<div id="post-footer-2" class="post-meta">
				<time class="post-date" datetime="2014-12-16">
					2014-Dec-16
				</time>
			</div>
		</article>

		<hr class="style-hr">

		<article class="post">
			<div id="post-header-1" class="post-header">
				<h2 class="post-title"> SI206 Personal Page Assignment </h2>
			</div>
			<section class="post-excerpt">
				<h2>Four pages are created for this assignment:</h2>
				<ul>
					<li>index.php</li>
					<li>photo.php</li>
					<li>about_me.php</li>
					<li>default.php</li>
				</ul>
				<p>	All links in the navigation bar have been tested.<br>
					As described on ctools, the tasks are completed in smaller pieces.<br>
					The home page (index.php) serves as a main template for most updated articles.<br>
					The photo page (photo.php) has 10 sample images which are styled with bootstrap.<br>
					The about me page (about_me.php) contains brief information about myself.<br>
					The default page notifies users that the website is currently under construction. (Let's see how far it goes =.=||| Not sure if I will continute update the site after the course is done!).
				</p>
			</section>
			<div id="post-footer-1" class="post-meta">
				<time class="post-date" datetime="2014-11-24">
					2014-Nov-24
				</time>
			</div>
		</article>

		<hr class="style-hr">
		</div>
	</div>

	<?php
		include 'footer.php';
	?>

</body>
</html>