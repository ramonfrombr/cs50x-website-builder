Now turn to implementing `compute_score`. To compute the score of a word, you need to know the point value of each letter in the word. You can associate letters and their point values with an _array_. Imagine an array of 26 `int`s, called `POINTS`, in which the first number is the point value for ‘A’, the second number is the point value for ‘B’, and so on. By declaring and initializing such an array outside of any single function, you can ensure this array is accessible to any function, including `compute_score`.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Points assigned to each letter of the alphabet
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string word);

    int main(void)
    {
        // Prompt the user for two words
        string word1 = get_string("Player 1: ");
        string word2 = get_string("Player 2: ");

        // Compute the score of each word
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Print the winner
    }

    int compute_score(string word)
    {
        // Compute and return score for word
    }

To implement `compute_score`, first try to find the point value of a single letter in `word`.

- Recall that to find the character at the nth index of a string, `s`, you can write `s[n]`. So `word[0]`, for example, will give you the first character of `word`.
- Now, recall that computers represent characters using [ASCII](http://asciitable.com/), a standard that represents each character as a number.
- Recall too that the 0th index of `POINTS`, `POINTS[0]`, gives you the point value of ‘A’. Think about how you could transform the numeric representation of ‘A’ into the index of its point value. Now, what about ‘a’? You’ll need to apply different transformations to upper- and lower-case letters, so you may find the functions [`isupper`](https://manual.cs50.io/3/isupper) and [`islower`](https://manual.cs50.io/3/islower) to be helpful to you.
- Keep in mind that characters that are _not_ letters should be given zero points For example, `!` is worth 0 points.

If you can properly calculate the value of _one_ character in `words`, odds are you can use a loop to sum the points for the rest of the characters. Once you’ve tried the above on your own, consider this (quite revealing!) hint below.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Points assigned to each letter of the alphabet
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string word);

    int main(void)
    {
        // Prompt the user for two words
        string word1 = get_string("Player 1: ");
        string word2 = get_string("Player 2: ");

        // Compute the score of each word
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Print the winner
    }

    int compute_score(string word)
    {
        // Keep track of score
        int score = 0;

        // Compute score for each character
        for (int i = 0, len = strlen(word); i < len; i++)
        {
            if (isupper(word[i]))
            {
                score += POINTS[word[i] - 'A'];
            }
            else if (islower(word[i]))
            {
                score += POINTS[word[i] - 'a'];
            }
        }

        return score;
    }
