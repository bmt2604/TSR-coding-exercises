/**
* Returns the number of vowels and consonants in a string.
*/
function countLetters(str) {
	
	const vowels = ["a", "e", "i", "o", "u"];
	const consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", 
						"q", "r", "s", "t", "v", "w", "x", "y", "z"];

	var vowelCount = 0;
	var consonantCount = 0;
	
	for (let letter of str) {
		if (vowels.includes(letter.toLowerCase())) {
			vowelCount++;
		} else if (consonants.includes(letter.toLowerCase())) {
			consonantCount++;
		}
	}
	
	return "Vowels: " + vowelCount + ", Consonants: " + consonantCount;
}