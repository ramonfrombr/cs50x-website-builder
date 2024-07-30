# Mario

![screenshot of Mario jumping up pyramid](https://cs50.harvard.edu/x/2024/psets/6/mario/less/pyramid.png)

## Problem to Solve

In a file called `mario.py` in a folder called `sentimental-mario-less`, write a program that recreates a half-pyramid using hashes (`#`) for blocks, exactly as you did in [Problem Set 1](../../../1/). Your program this time should be written in Python!

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-sUSilCTveD7JTV2lOZ7eIqKbo" src="https://asciinema.org/a/sUSilCTveD7JTV2lOZ7eIqKbo.js"></script>

## Specification

- To make things more interesting, first prompt the user with `get_int` for the half-pyramid’s height, a positive integer between `1` and `8`, inclusive.
- If the user fails to provide a positive integer no greater than `8`, you should re-prompt for the same again.
- Then, generate (with the help of `print` and one or more loops) the desired half-pyramid.
- Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.

## How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

- Run your program as `python mario.py` and wait for a prompt for input. Type in `-1` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
- Run your program as `python mario.py` and wait for a prompt for input. Type in `0` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
- Run your program as `python mario.py` and wait for a prompt for input. Type in `1` and press enter. Your program should generate the below output. Be sure that the pyramid is aligned to the bottom-left corner of your terminal, and that there are no extra spaces at the end of each line.

        #

- Run your program as `python mario.py` and wait for a prompt for input. Type in `2` and press enter. Your program should generate the below output. Be sure that the pyramid is aligned to the bottom-left corner of your terminal, and that there are no extra spaces at the end of each line.

         #
        ##

- Run your program as `python mario.py` and wait for a prompt for input. Type in `8` and press enter. Your program should generate the below output. Be sure that the pyramid is aligned to the bottom-left corner of your terminal, and that there are no extra spaces at the end of each line.

               #
              ##
             ###
            ####
           #####
          ######
         #######
        ########

- Run your program as `python mario.py` and wait for a prompt for input. Type in `9` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number. Then, type in `2` and press enter. Your program should generate the below output. Be sure that the pyramid is aligned to the bottom-left corner of your terminal, and that there are no extra spaces at the end of each line.

         #
        ##

- Run your program as `python mario.py` and wait for a prompt for input. Type in `foo` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
- Run your program as `python mario.py` and wait for a prompt for input. Do not type anything, and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.

### Correctness

    check50 cs50/problems/2024/x/sentimental/mario/less

### Style

    style50 mario.py

## How to Submit

    submit50 cs50/problems/2024/x/sentimental/mario/less
