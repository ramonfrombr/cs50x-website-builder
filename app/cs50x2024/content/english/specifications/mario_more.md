# Mario

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cWOkHQXw0JQ?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=11"></iframe></div>

## Problem to Solve

Toward the beginning of World 1-1 in Nintendo’s Super Mario Brothers, Mario must hop over adjacent pyramids of blocks, per the below.

![screenshot of Mario jumping over adjacent pyramids](https://cs50.harvard.edu/x/2024/psets/1/mario/more/pyramids.png)

In a file called `mario.c` in a folder called `mario-more`, implement a program in C that recreates that pyramid, using hashes (`#`) for bricks, as in the below:

       #  #
      ##  ##
     ###  ###
    ####  ####

And let’s allow the user to decide just how tall the pyramids should be by first prompting them for a positive `int` between, say, 1 and 8, inclusive.

#### Examples

Here’s how the program might work if the user inputs `8` when prompted:

    $ ./mario
    Height: 8
           #  #
          ##  ##
         ###  ###
        ####  ####
       #####  #####
      ######  ######
     #######  #######
    ########  ########

Here’s how the program might work if the user inputs `4` when prompted:

    $ ./mario
    Height: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Here’s how the program might work if the user inputs `2` when prompted:

    $ ./mario
    Height: 2
     #  #
    ##  ##

And here’s how the program might work if the user inputs `1` when prompted:

    $ ./mario
    Height: 1
    #  #

If the user doesn’t, in fact, input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Notice that width of the “gap” between adjacent pyramids is equal to the width of two hashes, irrespective of the pyramids’ heights.

### Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/FzN9RAjYG_Q?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### How to Test Your Code

Does your code work as prescribed when you input

- `-1` (or other negative numbers)?
- `0`?
- `1` through `8`?
- `9` or other positive numbers?
- letters or words?
- no input at all, when you only hit Enter?

You can also execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

### Correctness

In your terminal, execute the below to check your work’s correctness.

    check50 cs50/problems/2024/x/mario/more

### Style

Execute the below to evaluate the style of your code using `style50`.

    style50 mario.c

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2024/x/mario/more
