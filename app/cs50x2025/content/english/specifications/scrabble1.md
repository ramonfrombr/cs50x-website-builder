# Scrabble

![Scrabble Board](https://cs50.harvard.edu/x/2024/psets/2/scrabble/scrabble.png)

## Problem to Solve

In the game of [Scrabble](https://scrabble.hasbro.com/en-us/rules), players create words to score points, and the number of points is the sum of the point values of each letter in the word.

| A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 3   | 3   | 2   | 1   | 4   | 2   | 4   | 1   | 8   | 5   | 1   | 3   | 1   | 1   | 3   | 10  | 1   | 1   | 1   | 1   | 4   | 4   | 8   | 4   | 10  |

For example, if we wanted to score the word “CODE”, we would note that the ‘C’ is worth 3 points, the ‘O’ is worth 1 point, the ‘D’ is worth 2 points, and the ‘E’ is worth 1 point. Summing these, we get that “CODE” is worth 7 points.

In a file called `scrabble.c` in a folder called `scrabble`, implement a program in C that determines the winner of a short Scrabble-like game. Your program should prompt for input twice: once for “Player 1” to input their word and once for “Player 2” to input their word. Then, depending on which player scores the most points, your program should either print “Player 1 wins!”, “Player 2 wins!”, or “Tie!” (in the event the two players score equal points).

## Demo

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-74B4kq3ftleKe6AdN0NxFV8CN" src="https://asciinema.org/a/74B4kq3ftleKe6AdN0NxFV8CN.js"></script>

## Advice

### Write some code that you know will compile

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {

    }

Notice that you’ve now included a few header files that will give you access to functions which might help you solve this problem.

### Write some pseudocode before writing more code

If unsure how to solve the problem itself, break it down into smaller problems that you can probably solve first. For instance, this problem is really only a handful of problems:

1.  Prompt for the user for two words
2.  Compute the score of each word
3.  Print the winner

Let’s write some pseudcode as comments to remind you to do just that:

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Prompt the user for two words

        // Compute the score of each word

        // Print the winner
    }

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Some problems in problem sets, like this one, might contain spoilers (like the next one) that ultimately walk you through the entire solution. While you are permitted to use this code, we really do strongly encourage you to try things out yourself first! The other problems in the problem set won’t have this sort of walkthrough, and typically the problem that contains the “full spoiler” is a warm-up version of the bigger problem you’ll later need to tackle.</p></div>

### Convert the pseudocode to code

First, consider how you might prompt the user for two words. Recall that `get_string`, a function in the CS50 library, can prompt the user for a string.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Prompt the user for two words
        string word1 = get_string("Player 1: ");
        string word2 = get_string("Player 2: ");

        // Compute the score of each word

        // Print the winner
    }

Next consider how to compute the score of each word. Since the same scoring algorithm applies to both words, you have a good opportunity for _abstraction_. Here we’ll define a function called `compute_score` that takes a string, called `word`, as input, and then returns `word`’s score as an `int`.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

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
