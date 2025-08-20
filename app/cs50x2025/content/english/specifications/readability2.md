### Convert the pseudocode to code

First, consider how you might prompt the user for some text. Recall that `get_string`, a function in the CS50 library, can prompt the user for a string.

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Prompt the user for some text
        string text = get_string("Text: ");

        // Count the number of letters, words, and sentences in the text

        // Compute the Coleman-Liau index

        // Print the grade level
    }

Now that you’ve collected input from the user, you can begin to analyze that input. First, try to count the number of letters in the text. Consider letters to be uppercase or lowercase alphabetical character, not punctuation, digits, or other symbols.

One way to approach this problem is to create a function called `count_letters` that takes a string, `text`, as input, and then returns the number of letters in that text as an `int`.

    int count_letters(string text)
    {
        // Return the number of letters in text
    }

You’ll need to write your own code to count the number of letters in the text. But someone more experienced than you may have already written a function to determine if a character is alphabetical. This is a good opportunity to use the [CS50 manual](https://manual.cs50.io/), a collection of explanations of common functions in the C Standard Library.

You can integrate `count_letters` into the code you’ve already written, as follows.

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string text);

    int main(void)
    {
        // Prompt the user for some text
        string text = get_string("Text: ");

        // Count the number of letters, words, and sentences in the text
        int letters = count_letters(text);

        // Compute the Coleman-Liau index

        // Print the grade level
    }

    int count_letters(string text)
    {
        // Return the number of letters in text
    }

Next, write a function to count words.

    int count_words(string text)
    {
        // Return the number of words in text
    }

For the purpose of this problem, we’ll consider any sequence of characters separated by a space to be a word (so a hyphenated word like “sister-in-law” should be considered one word, not three). You may assume that a sentence:

- will contain at least one word;
- will not start or end with a space; and
- will not have multiple spaces in a row.

Under those assumptions, you might be able to find a relationship between the number words and the number of spaces. You are, of course, welcome to attempt a solution that will tolerate multiple spaces between words or indeed, no words!

You can now integrate `count_words` into your program as follows:

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string text);
    int count_words(string text);

    int main(void)
    {
        // Prompt the user for some text
        string text = get_string("Text: ");

        // Count the number of letters, words, and sentences in the text
        int letters = count_letters(text);
        int words = count_words(text);

        // Compute the Coleman-Liau index

        // Print the grade level
    }

    int count_letters(string text)
    {
        // Return the number of letters in text
    }

    int count_words(string text)
    {
        // Return the number of words in text
    }

Finally, write a function to count sentences. You can consider any sequence of characters that ends with a `.` or a `!` or a `?` to be a sentence.

    int count_sentences(string text)
    {
        // Return the number of sentences in text
    }
