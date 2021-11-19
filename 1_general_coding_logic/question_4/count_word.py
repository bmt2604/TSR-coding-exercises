import string


def remove_punctuation(text):
    """Removes punctuation from a string of text."""

    new_text = text

    for character in new_text:
        if character in string.punctuation:
            new_text = new_text.replace(character, "")

    return new_text


def count_word(text, word):
    """Returns the number of occurrences of a given word
    in a string of text."""

    # remove punctuation and split into words
    words = remove_punctuation(text).split(" ")

    count = 0

    for i in words:
        if i.lower() == word.lower():
            count += 1

    return "The word {} was found {} time(s).".format(word, count)


print(count_word("This is a test. Test the word 'test'!", "test"))
