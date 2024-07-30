Finally, finish your pseudocode’s last step: printing the winner. Recall that an `if` statement can be used to check if a condition is true, and that the additional usage of `else if` or `else` can check for other (exclusive) conditions.

    if (/* Player 1 wins */)
    {
        // ...
    }
    else if (/* Player 2 wins */)
    {
        // ...
    }
    else
    {
        // ...
    }

And once you’ve tried the above, feel free to take a peek at the hint (or, rather, complete solution!) below.

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
        if (score1 > score2)
        {
            printf("Player 1 wins!\n");
        }
        else if (score1 < score2)
        {
            printf("Player 2 wins!\n");
        }
        else
        {
            printf("Tie!\n");
        }
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

## How to Test

Your program should behave per the examples below.

    $ ./scrabble
    Player 1: Question?
    Player 2: Question!
    Tie!


    $ ./scrabble
    Player 1: red
    Player 2: wheelbarrow
    Player 2 wins!


    $ ./scrabble
    Player 1: COMPUTER
    Player 2: science
    Player 1 wins!


    $ ./scrabble
    Player 1: Scrabble
    Player 2: wiNNeR
    Player 1 wins!

### Correctness

In your terminal, execute the below to check your work’s correctness.

    check50 cs50/problems/2024/x/scrabble

### Style

Execute the below to evaluate the style of your code using `style50`.

    style50 scrabble.c

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2024/x/scrabble
