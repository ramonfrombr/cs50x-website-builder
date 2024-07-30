# Hello, It’s Me

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/YQHsXMglC9A?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=74"></iframe></div>

## Problem to Solve

In a file called `hello.c`, in a folder called `me`, implement a program in C that prompts the user for their name and then says hello to that user. For instance, if the user’s name is Adele, your program should print `hello, Adele\n`!

#### Hints

- Recall that you can get a `string` from a user with `get_string`, which is declared in `cs50.h`.
- Recall that you can print a `string` with `printf`, which is declared in `stdio.h`.
- Recall that you can format a `string` with `printf` with `%s`.

## Demo

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-Jn4egWrG0Rvuzo9d2Rs0qpkcL" src="https://asc
iinema.org/a/Jn4egWrG0Rvuzo9d2Rs0qpkcL.js"></script>

## How to Begin

Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    mkdir me

to make a folder called `me` in your codespace.

Then execute

    cd me

to change directories into that folder. You should now see your terminal prompt as `me/ $`. You can now execute

    code hello.c

to create a file called `hello.c` in which you can write your code.

## Walkthrough

Here’s a “walkthrough” (i.e., tour) of this problem, if you’d like a verbal overview of what to do too!

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/wSk1KSDUEYA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## How to Test

### Correctness

In your terminal, execute the below to check your work’s correctness.

    check50 cs50/problems/2024/x/me

### Style

    style50 hello.c

## How to Submit

    submit50 cs50/problems/2024/x/me
