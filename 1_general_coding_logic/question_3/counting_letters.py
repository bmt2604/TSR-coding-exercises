def count_letters(text):
    """Returns the number of vowels and consonants in a string."""

    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                  "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    vowel_count = 0
    consonant_count = 0

    for letter in text:
        if letter.lower() in vowels:
            vowel_count += 1
        elif letter.lower() in consonants:
            consonant_count += 1

    return "Vowels: {}, Consonants: {}".format(vowel_count, consonant_count)
