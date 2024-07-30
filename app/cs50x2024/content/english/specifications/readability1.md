# Readability

![Charlotte's Web Cover](https://cs50.harvard.edu/x/2024/psets/2/readability/charlottes_web.jpg)

## Problem to Solve

According to [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), E.B. White’s _Charlotte’s Web_ is between a second- and fourth-grade reading level, and Lois Lowry’s _The Giver_ is between an eighth- and twelfth-grade reading level. What does it mean, though, for a book to be at a particular reading level?

Well, in many cases, a human expert might read a book and make a decision on the grade (i.e., year in school) for which they think the book is most appropriate. But an algorithm could likely figure that out too!

In a file called `readability.c` in a folder called `readability`, you’ll implement a program that calculates the approximate grade level needed to comprehend some text. Your program should print as output “Grade X” where “X” is the grade level computed, rounded to the nearest integer. If the grade level is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output “Grade 16+” instead of giving the exact index number. If the grade level is less than 1, your program should output “Before Grade 1”.

## Demo

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script>

## Background

So what sorts of traits are characteristic of higher reading levels? Well, longer words probably correlate with higher reading levels. Likewise, longer sentences probably correlate with higher reading levels, too.

A number of “readability tests” have been developed over the years that define formulas for computing the reading level of a text. One such readability test is the _Coleman-Liau index_. The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text. The formula is

    index = 0.0588 * L - 0.296 * S - 15.8

where `L` is the average number of letters per 100 words in the text, and `S` is the average number of sentences per 100 words in the text.

## Advice

### Write some code that you know will compile

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {

    }

Notice that you’ve now included a few header files that will give you access to functions which might help you solve this problem.

### Write some pseudocode before writing more code

If unsure how to solve the problem itself, break it down into smaller problems that you can probably solve first. For instance, this problem is really only a handful of problems:

1.  Prompt the user for some text
2.  Count the number of letters, words, and sentences in the text
3.  Compute the Coleman-Liau index
4.  Print the grade level

Let’s write some pseudcode as comments to remind you to do just that:

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Prompt the user for some text

        // Count the number of letters, words, and sentences in the text

        // Compute the Coleman-Liau index

        // Print the grade level
    }
