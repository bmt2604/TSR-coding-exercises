/**
* Checks if username input is valid. Displays a message if username is invalid.
*/
function validateUsername() {
	var input = document.getElementById("username").value;
	// check for emptiness, spaces and symbols		
	if ((input.trim() != "") && (input.indexOf(' ') == -1) && (input.match("^[A-Za-z0-9]+$"))) {
		document.getElementById("msg").innerHTML = "";
		return true;
	} else {
		document.getElementById("msg").innerHTML = "Please enter a valid username.";
		return false;
	}
}