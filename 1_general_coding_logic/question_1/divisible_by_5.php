<!DOCTYPE html>
<html lang="en">

<body>

<?php

/**
* Returns "true" if n is evenly divisible by 5. Otherwise, "false".
*/
function divisible_by_5(int $n) {
	if (($n % 5) == 0) {
    	return "true";
    } else {
    	return "false";
    }
}

?>

</body>
</html>