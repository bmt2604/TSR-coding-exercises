/**
* Returns the number of occurrences of a given word in a string of text.
*/
function countWord(str, word) {
	// remove punctuation
	var newString = str.replace(/['!"#$%&\\'()\*+,\-\.\/:;<=>?@\[\\\]\^_`{|}~']/g,"");
	
	// split into words
	var words = newString.split(" ");
	
	var count = 0;
	
	for (let i of words) {
		if (i.toLowerCase() == word.toLowerCase()) {
			count += 1;
		}
	}
	return "The word " + word + " was found " + count.toString() + " time(s).";
}