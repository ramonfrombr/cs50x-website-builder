# Speller

## Problem to Solve

For this problem, you’ll implement a program that spell-checks a file, a la the below, using a hash table.

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-o01nuZNSBSH2khVokTs2GEPtP" src="https://asciinema.org/a/o01nuZNSBSH2khVokTs2GEPtP.js"></script>

## Distribution Code

For this problem, you’ll extend the functionality of code provided to you by CS50’s staff.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2023/fall/psets/5/speller.zip

in order to download a ZIP called `speller.zip` into your codespace.

Then execute

    unzip speller.zip

to create a folder called `speller`. You no longer need the ZIP file, so you can execute

    rm speller.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd speller

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    speller/ $

Execute `ls` by itself, and you should see a few files and folders:

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

## Background

<div class="alert alert-danger" data-alert="danger" role="alert"><p><strong>Given the many files in this program, it’s important to read this section in its entirety before starting. You’ll then know what to do and how to do it!</strong></p></div>

Theoretically, on input of size _n_, an algorithm with a running time of _n_ is “asymptotically equivalent,” in terms of _O_, to an algorithm with a running time of _2n_. Indeed, when describing the running time of an algorithm, we typically focus on the dominant (i.e., most impactful) term (i.e., _n_ in this case, since _n_ could be much larger than 2). In the real world, though, the fact of the matter is that _2n_ feels twice as slow as _n_.

The challenge ahead of you is to implement the fastest spell checker you can! By “fastest,” though, we’re talking actual “wall-clock,” not asymptotic, time.

In `speller.c`, we’ve put together a program that’s designed to spell-check a file after loading a dictionary of words from disk into memory. That dictionary, meanwhile, is implemented in a file called `dictionary.c`. (It could just be implemented in `speller.c`, but as programs get more complex, it’s often convenient to break them into multiple files.) The prototypes for the functions therein, meanwhile, are defined not in `dictionary.c` itself but in `dictionary.h` instead. That way, both `speller.c` and `dictionary.c` can `#include` the file. Unfortunately, we didn’t quite get around to implementing the loading part. Or the checking part. Both (and a bit more) we leave to you! But first, a tour.

### Understanding

#### `dictionary.h`

Open up `dictionary.h`, and you’ll see some new syntax, including a few lines that mention `DICTIONARY_H`. No need to worry about those, but, if curious, those lines just ensure that, even though `dictionary.c` and `speller.c` (which you’ll see in a moment) `#include` this file, `clang` will only compile it once.

Next notice how we `#include` a file called `stdbool.h`. That’s the file in which `bool` itself is defined. You’ve not needed it before, since the CS50 Library used to `#include` that for you.

Also notice our use of `#define`, a “preprocessor directive” that defines a “constant” called `LENGTH` that has a value of `45`. It’s a constant in the sense that you can’t (accidentally) change it in your own code. In fact, `clang` will replace any mentions of `LENGTH` in your own code with, literally, `45`. In other words, it’s not a variable, just a find-and-replace trick.

Finally, notice the prototypes for five functions: `check`, `hash`, `load`, `size`, and `unload`. Notice how three of those take a pointer as an argument, per the `*`:

    bool check(const char *word);
    unsigned int hash(const char *word);
    bool load(const char *dictionary);

Recall that `char *` is what we used to call `string`. So those three prototypes are essentially just:

    bool check(const string word);
    unsigned int hash(const string word);
    bool load(const string dictionary);

And `const`, meanwhile, just says that those strings, when passed in as arguments, must remain constant; you won’t be able to change them, accidentally or otherwise!

#### `dictionary.c`

Now open up `dictionary.c`. Notice how, atop the file, we’ve defined a `struct` called `node` that represents a node in a hash table. And we’ve declared a global pointer array, `table`, which will (soon) represent the hash table you will use to keep track of words in the dictionary. The array contains `N` node pointers, and we’ve set `N` equal to `26` for now, to match with the default `hash` function as described below. You will likely want to increase this depending on your own implementation of `hash`.

Next, notice that we’ve implemented `load`, `check`, `size`, and `unload`, but only barely, just enough for the code to compile. Notice too that we’ve implemented `hash` with a sample algorithm based on the first letter of the word. Your job, ultimately, is to re-implement those functions as cleverly as possible so that this spell checker works as advertised. And fast!
