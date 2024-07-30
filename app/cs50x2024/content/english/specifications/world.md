# Hello, World

## Problem to Solve

Thanks to Professor [David Malan](https://en.wikipedia.org/wiki/David_J._Malan) (who taught CS50 when Ramon took it!), “hello, world” has been implemented in hundreds of languages. Let’s add your implementation to the list!

In a file called `hello.c`, in a folder called `world`, implement a program in C that prints `hello, world\n`, and that’s it!

#### Hint

Here’s the actual code you should write! (Quite the hint, huh?) Best to type it yourself, though, rather than copy/paste, so that you start to develop some “muscle memory” for writing code.

    #include <stdio.h>

    int main(void)
    {
        printf("hello, world\n");
    }

## Demo

Here’s a demo of what should happen when you compile and execute your program.

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-C5rag3703OZpKxGJ6dSwHnUEF" src="https://asciinema.org/a/C5rag3703OZpKxGJ6dSwHnUEF.js"></script>

## How to Begin

Open [VS Code](https://cs50.dev/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $

Next execute

    mkdir world

to make a folder called `world` in your codespace.

Then execute

    cd world

to change directories into that folder. You should now see your terminal prompt as `world/ $`. You can now execute

    code hello.c

to create a file called `hello.c` in which you can write your code.

## How to Test

Recall that you can compile `hello.c` with:

    make hello

If you don’t see an error message, it compiled successfully! You can confirm as much with

    ls

which should list not only `hello.c` (which is source code) but also `hello` (which is machine code).

If you do see an error message, try to fix your code and try to compile it again. If you don’t understand the error message, though, try executing

    help50 make hello

for advice.

Once your code compiles successfully, you can execute your program with:

    ./hello

### Correctness

Execute the below to evaluate the correctness of your code using `check50`, a command-line program that will output happy faces whenever your code passes CS50’s automated tests and sad faces whenever it doesn’t!

    check50 cs50/problems/2024/x/world

### Style

Execute the below to evaluate the style of your code using `style50`, a command-line program that will output additions (in green) and deletions (in red) that you should make to your program in order to improve its style. If you have trouble seeing those colors, `style50` supports other [modes](https://cs50.readthedocs.io/style50/) too!

    style50 hello.c

## How to Submit

No need to submit this one!
