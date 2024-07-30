### Implement `size`

Complete the `size` function. `size` should return the number of words loaded in the dictionary. Consider two approaches to this problem:

- Count each word as you load it into the dictionary. Return that count when `size` is called.
- Each time `size` is called, iterate through the words in the hash table to count them up. Return that count.

Which seems most efficient to you? Whichever you choose, we’ll leave the code up to you.

### Implement `check`

Complete the `check` function. `check` should return `true` if a word is located in the dictionary, otherwise `false`.

Consider that this problem is also composed of smaller problems. If you’ve implemented a hash table, finding a word takes only a few steps:

1.  Hash the word to obtain its hash value
2.  Search the hash table at the location specified by the word’s hash value
    1.  Return `true` if the word is found
3.  Return `false` if no word is found

To compare two strings case-insensitively, you may find [`strcasecmp`](https://man.cs50.io/3/strcasecmp) (declared in `strings.h`) useful! You’ll likely also want to ensure that your hash function is case-insensitive, such that `foo` and `FOO` have the same hash value.

### Implement `unload`

Complete the `unload` function. Be sure to `free` in `unload` any memory that you allocated in `load`!

Recall that `valgrind` is your newest best friend. Know that `valgrind` watches for leaks while your program is actually running, so be sure to provide command-line arguments if you want `valgrind` to analyze `speller` while you use a particular `dictionary` and/or text, as in the below. Best to use a small text, though, else `valgrind` could take quite a while to run.

    valgrind ./speller texts/cat.txt

If you run `valgrind` without specifying a `text` for `speller`, your implementations of `load` and `unload` won’t actually get called (and thus analyzed).

If unsure how to interpret the output of `valgrind`, do just ask `help50` for help:

    help50 valgrind ./speller texts/cat.txt

## Walkthroughs

<div class="alert alert-danger" data-alert="danger" role="alert"><p><strong>Note that there are 6 videos in this playlist.</strong></p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>

## How to Test

How to check whether your program is outting the right misspelled words? Well, you’re welcome to consult the “answer keys” that are inside of the `keys` directory that’s inside of your `speller` directory. For instance, inside of `keys/lalaland.txt` are all of the words that your program _should_ think are misspelled.

You could therefore run your program on some text in one window, as with the below.

    ./speller texts/lalaland.txt

And you could then run the staff’s solution on the same text in another window, as with the below.

    ./speller50 texts/lalaland.txt

And you could then compare the windows visually side by side. That could get tedious quickly, though. So you might instead want to “redirect” your program’s output to a file, as with the below.

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt

You can then compare both files side by side in the same window with a program like `diff`, as with the below.

    diff -y student.txt staff.txt

Alternatively, to save time, you could just compare your program’s output (assuming you redirected it to, e.g., `student.txt`) against one of the answer keys without running the staff’s solution, as with the below.

    diff -y student.txt keys/lalaland.txt

If your program’s output matches the staff’s, `diff` will output two columns that should be identical except for, perhaps, the running times at the bottom. If the columns differ, though, you’ll see a `>` or `|` where they differ. For instance, if you see

    MISSPELLED WORDS                                                MISSPELLED WORDS

    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L

that means your program (whose output is on the left) does not think that `Thelonious` or `MIA` is misspelled, even though the staff’s output (on the right) does, as is implied by the absence of, say, `Thelonious` in the lefthand column and the presence of `Thelonious` in the righthand column.

Finally, be sure to test with both the default large and small dictionaries. Be careful not to assume that if your solution runs successfully with the large dictionary it will also run successfully with the small one. Here’s how to try the small dictionary:

    ./speller dictionaries/small texts/cat.txt

### Correctness

    check50 cs50/problems/2024/x/speller

### Style

    style50 dictionary.c

## Staff’s Solution

How to assess just how fast (and correct) your code is? Well, as always, feel free to play with the staff’s solution, as with the below, and compare its numbers against yours.

    ./speller50 texts/lalaland.txt

## How to Submit

    submit50 cs50/problems/2024/x/speller
