### Counting Command-Line Arguments

Whatever your pseudocode, let’s first write only the C code that checks whether the program was run with a single command-line argument before adding additional functionality.

Specifically, modify `main` in `caesar.c` in such a way that, if the user provides no command-line arguments, or two or more, the function prints `"Usage: ./caesar key\n"` and then returns `1`, effectively exiting the program. If the user provides exactly one command-line argument, the program should print nothing and simply return `0`. The program should thus behave per the below.

    $ ./caesar
    Usage: ./caesar key


    $ ./caesar 1 2 3
    Usage: ./caesar key


    $ ./caesar 1

#### Hints

- Recall that you can print with `printf`.
- Recall that a function can return a value with `return`.
- Recall that `argc` contains the number of command-line arguments passed to a program, plus the program’s own name.

### Checking the Key

Now that your program is (hopefully!) accepting input as prescribed, it’s time for another step.

Add to `caesar.c`, below `main`, a function called, e.g., `only_digits` that takes a `string` as an argument and returns `true` if that `string` contains only digits, `0` through `9`, else it returns `false`. Be sure to add the function’s prototype above `main` as well.

#### Hints

- Odds are you’ll want a prototype like:
  bool only_digits(string s);

  And be sure to include `cs50.h` atop your file, so that the compiler recognizes `string` (and `bool`).

- Recall that a `string` is just an array of `char`s.
- Recall that `strlen`, declared in `string.h`, calculates the length of a `string`.
- You might find `isdigit`, declared in `ctype.h`, to be helpful, per [manual.cs50.io](https://manual.cs50.io/). But note that it only checks one `char` at a time!

Then modify `main` in such a way that it calls `only_digits` on `argv[1]`. If that function returns `false`, then `main` should print `"Usage: ./caesar key\n"` and return `1`. Else `main` should simply return `0`. The program should thus behave per the below:

    $ ./caesar 42


    $ ./caesar banana
    Usage: ./caesar key

### Using the Key

Now modify `main` in such a way that it converts `argv[1]` to an `int`. You might find `atoi`, declared in `stdlib.h`, to be helpful, per [manual.cs50.io](https://manual.cs50.io/). And then use `get_string` to prompt the user for some plaintext with `"plaintext: "`.

Then, implement a function called, e.g., `rotate`, that takes a `char` as input and also an `int`, and rotates that `char` by that many positions if it’s a letter (i.e., alphabetical), wrapping around from `Z` to `A` (and from `z` to `a`) as needed. If the `char` is not a letter, the function should instead return the same `char` unchanged.

#### Hints

- Odds are you’ll want a prototype like:
  char rotate(char c, int n);

  A function call like
  rotate('A', 1)

  or even
  rotate('A', 27)

  should thus return `'B'`. And a function call like
  rotate('!', 13)

  should return `'!'`.

- Recall that you can explicitly “cast” a `char` to an `int` with `(int)`, and an `int` to a `char` with `(char)`. Or you can do so implicitly by simply treating one as the other.
- Odds are you’ll want to subtract the ASCII value of `'A'` from any uppercase letters, so as to treat `'A'` as `0`, `'B'` as `1`, and so forth, while performing arithmetic. And then add it back when done with the same.
- Odds are you’ll want to subtract the ASCII value of `'a'` from any lowercase letters, so as to treat `'a'` as `0`, `'b'` as `1`, and so forth, while performing arithmetic. And then add it back when done with the same.
- You might find some other functions declared in `ctype.h` to be helpful, per [manual.cs50.io](https://manual.cs50.io/).
- Odds are you’ll find `%` helpful when “wrapping around” arithmetically from a value like `25` to `0`.

Then modify `main` in such a way that it prints `"ciphertext: "` and then iterates over every `char` in the user’s plaintext, calling `rotate` on each, and printing the return value thereof.

#### Hints

- Recall that `printf` can print a `char` using `%c`.
- If you’re not seeing any output at all when you call `printf`, odds are it’s because you’re printing characters outside of the valid ASCII range from 0 to 127. Try printing characters temporarily as numbers (using `%i` instead of `%c`) to see what values you’re printing!

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/V2uusmv2wxI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## How to Test

### Correctness

In your terminal, execute the below to check your work’s correctness.

    check50 cs50/problems/2024/x/caesar

#### How to Use `debug50`

Looking to run `debug50`? You can do so as follows, after compiling your code successfully with `make`,

    debug50 ./caesar KEY

wherein `KEY` is the key you give as a command-line argument to your program. Note that running

    debug50 ./caesar

will (ideally!) cause your program end by prompting the user for a key.

### Style

Execute the below to evaluate the style of your code using `style50`.

    style50 caesar.c

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2024/x/caesar
