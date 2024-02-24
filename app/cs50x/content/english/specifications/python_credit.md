# Credit

## Problem to Solve

In a filed called `credit.py` in a folder called `sentimental-credit`, write a program that prompts the user for a credit card number and then reports (via `print`) whether it is a valid American Express, MasterCard, or Visa card number, exactly as you did in [Problem Set 1](../../1/). Your program this time should be written in Python!

## Demo

## Specification

-   So that we can automate some tests of your code, we ask that your program’s last line of output be `AMEX\n` or `MASTERCARD\n` or `VISA\n` or `INVALID\n`, nothing more, nothing less.
-   For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
-   Best to use `get_int` or `get_string` from CS50’s library to get users’ input, depending on how you to decide to implement this one.

## Hints

-   It’s possible to use regular expressions to validate user input. You might use Python’s [`re`](https://docs.python.org/3/library/re.html) module, for example, to check whether the user’s input is indeed a sequence of digits of the correct length.

## How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `378282246310005` and press enter. Your program should output `AMEX`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `371449635398431` and press enter. Your program should output `AMEX`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `5555555555554444` and press enter. Your program should output `MASTERCARD`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `5105105105105100` and press enter. Your program should output `MASTERCARD`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `4111111111111111` and press enter. Your program should output `VISA`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `4012888888881881` and press enter. Your program should output `VISA`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `1234567890` and press enter. Your program should output `INVALID`.

### Correctness

    check50 cs50/problems/2024/x/sentimental/credit

### Style

    style50 credit.py

## How to Submit

    submit50 cs50/problems/2024/x/sentimental/credit

### Why does my submission pass check50, but shows “No results” in my Gradebook after running submit50?

In some cases, `submit50` may not grade the assignment due to inconsistent formatting in your `credit.py` file. To fix this issue, run `black credit.py` in the `sentimental-credit` folder. Address any issues that are revealed. Run `check50` again to ensure your submission still functions. Finally, run the `submit50` command above again. Your result will appear in your [Gradebook](https://cs50.me/cs50x) within a few minutes.

Please note that if there is a numerical score next to your credit submission in the `submissions` area of your [Gradebook](https://cs50.me/cs50x), the procedure discussed above does not apply to you. Likely, you have not fully addressed the requirements of the problem set and should rely upon `check50` for clues as to what work remains.
