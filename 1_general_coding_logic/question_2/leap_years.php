<!DOCTYPE html>
<html lang="en">

<body>

<?php

/**
* Returns TRUE if year is a leap year. Otherwise, FALSE.
*/
function leap_year(int $year) {
	if (($year % 4) != 0) {
    	return FALSE;
    } elseif (($year % 100) != 0) {
    	return TRUE;
    } elseif (($year % 400) != 0) {
		return FALSE;
	} else {
		return FALSE;
	}
}
	
$current_year = 2021;
$count = 0;

while ($count != 20) {
	if (leap_year($current_year)) {
		echo $current_year;
		echo "<br>";
		$count += 1;
	}
	$current_year += 1;
}

?>

</body>
</html>