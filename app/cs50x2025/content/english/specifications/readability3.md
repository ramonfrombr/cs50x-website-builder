You can integrate `count_sentences` into your program as follows:

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string text);
    int count_words(string text);
    int count_sentences(string text);

    int main(void)
    {
        // Prompt the user for some text
        string text = get_string("Text: ");

        // Count the number of letters, words, and sentences in the text
        int letters = count_letters(text);
        int words = count_words(text);
        int sentences = count_sentences(text);

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

    int count_sentences(string text)
    {
        // Return the number of sentences in text
    }

Finally, compute the Coleman-Liau index and print the resulting grade level.

- Recall that the Coleman-Liau index is computed using `index = 0.0588 * L - 0.296 * S - 15.8`
- `L` is the average number of letters per 100 words in the text: that is, the number of letters divided by the number of words, all multiplied by 100.
- `S` is the average number of sentences per 100 words in the text: that is, the number of sentences divided by the number of words, all multiplied by 100.
- You’ll want to round the result to the nearest whole number, so recall that `round` is declared in `math.h`, per [manual.cs50.io](https://manual.cs50.io/).
- Recall that, when dividing values of type `int` in C, the result will also be an `int`, with any remainder (i.e., digits after the decimal point) discarded. Put another way, the result will be “truncated.” You might want to cast your one or more values to `float` before performing division when calculating `L` and `S`!

If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output “Grade 16+” instead of outputting an exact index number. If the index number is less than 1, your program should output “Before Grade 1”.

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/AOVyZEh9zgE?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## How to Test

Try running your program on the following texts, to ensure you see the specified grade level. Be sure to copy only the text, no extra spaces.

- `One fish. Two fish. Red fish. Blue fish.` (Before Grade 1)
- `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` (Grade 2)
- `Congratulations! Today is your day. You're off to Great Places! You're off and away!` (Grade 3)
- `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` (Grade 5)
- `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` (Grade 7)
- `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` (Grade 8)
- `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` (Grade 8)
- `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` (Grade 9)
- `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` (Grade 10)
- `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` (Grade 16+)

### Correctness

In your terminal, execute the below to check your work’s correctness.

    check50 cs50/problems/2024/x/readability

### Style

Execute the below to evaluate the style of your code using `style50`.

    style50 readability.c

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2024/x/readability
