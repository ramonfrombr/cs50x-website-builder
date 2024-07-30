# Hello, Again

## Problem to Solve

In a file called `hello.py` in a folder called `sentimental-hello`, implement a program that prompts a user for their name, and then prints `hello, so-and-so`, where `so-and-so` is their provided name, exactly as you did in [Problem Set 1](../../1/). Except that your program this time should be written in Python!

### Hints

- Recall that you can get a `str` from a user with `get_string`, which is declared in the `cs50` library.
- Recall that you can print a `str` with `print`.
- Recall that you can create formatted strings in Python by prepending `f` to a string itself. For example, `f"{name}"` will substitute (“interpolate”) the value of the variable `name` where you’ve written `{name}`.

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-gqi2voQFzbKlna6WkQR0G2W93" src="https://asciinema.org/a/gqi2voQFzbKlna6WkQR0G2W93.js"></script>

## How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

- Run your program as `python hello.py`, and wait for a prompt for input. Type in `David` and press enter. Your program should output `hello, David`.
- Run your program as `python hello.py`, and wait for a prompt for input. Type in `Inno` and press enter. Your program should output `hello, Inno`.
- Run your program as `python hello.py`, and wait for a prompt for input. Type in `Kamryn` and press enter. Your program should output `hello, Kamryn`.

### Correctness

    check50 cs50/problems/2024/x/sentimental/hello

### Style

    style50 hello.py

## How to Submit

    submit50 cs50/problems/2024/x/sentimental/hello
