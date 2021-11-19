<?php session_start(); ?>

<!DOCTYPE html>
<html lang="en">

<head>
	<title>Confirmation Page</title>
	<link href="mystyles.css" type="text/css" rel="stylesheet">
	<script src="validate_username.js"></script>
</head>

<body>	
<div class="container1">
	<h2>Log in to your account</h2>
	<hr>
	<div class="container2">

		<?php
		if (isset($_POST['username']) && isset($_POST['password'])) {
		
			if ($_POST['username'] == "admin" && $_POST['password'] == "letmein") {
				echo "<h1>Welcome, ".$_POST['username']."!</h1>";
	
			} else {
				echo "Log in was unsuccessful. Please try again.</div>";
				echo '<form action="welcome.php" onsubmit="return validateUsername();" method="POST">
						<div id="userInput">
							<label for="username">Username</label><br>
							<input type="text" id="username" name="username" autocomplete="off" required>
							<p id="msg"></p>
							<br>
							<label for="password">Password</label><br>
							<input type="password" id="password" name="password" required>
						</div>
						<br>
						<br>
						<input type="submit" id="button" value="Log in">
					</form>';
			}
		}
		?>

</div>
</body>
</html>