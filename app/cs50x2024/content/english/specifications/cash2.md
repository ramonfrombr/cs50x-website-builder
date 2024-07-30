### Convert the pseudocode to code

First, consider how you might prompt the user for the cents they are owed. Recall that a `do while` loop is helpful when you want to do something at least once, and possibly again and again, as in the below:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Prompt the user for change owed, in cents
        int cents;
        do
        {
            cents = get_int("Change owed: ");
        }
        while (cents < 0);
    }

It’s wise to stop here and `make` your program. Test to be sure your program compiles, and that it reprompts you if you enter less than 0 cents (or if you enter an input like “cat”).

Next, consider how to calculate how many quarters you should give the customer. Since we’re using a greedy algorithm, this question becomes “what’s the _greatest_ number of quarters could you give them?”. You _could_ write a solution to this problem in your `main` function. But, it might clear up your thinking to write a new function: one called `calculate_quarters`. That way you can better focus on the logic to calculate quarters. Later, you can integrate this function into your larger solution.

    int calculate_quarters(int cents)
    {
        // Calculate how many quarters you should give customer
    }

Notice that this function is indeed named `calculate_quarters`. Per `int cents` in parentheses, it takes an `int` called `cents` as input. And, per the `int` in front of its name, it should also “return” an `int`. That is, the output of this function is an integer: the number of quarters that fit into cents. If curious about this idea, recall there are several sample programs in Week 1’s [Source Code](https://github.com/cs50/lectures/tree/2023/fall/1/src1) that illustrate how functions can return a value.

Now consider this way of implementing `calculate_quarters` by adding to the number of quarters until we’ve run out of cents to convert to quarters:

    int calculate_quarters(int cents)
    {
        // Calculate how many quarters you should give customer
        int quarters = 0;
        while (cents >= 25)
        {
            quarters++;
            cents = cents - 25;
        }
        return quarters;
    }

Granted, there is at least one simpler way to solve this `calculate_quarters` problem. But we’ll leave that up to you to figure out!

With `calculate_quarters` functioning as intended, you can integrate this function into your program. Take care to “declare” the function’s “signature” (i.e., `int calculate_quarters(int cents)`) above your `main` function, so you can indeed use `calculate_quarters` there while defining it later, below `main`.

    #include <cs50.h>
    #include <stdio.h>

    int calculate_quarters(int cents);

    int main(void)
    {
        // Prompt the user for change owed, in cents
        int cents;
        do
        {
            cents = get_int("Change owed: ");
        }
        while (cents < 0);

        // Calculate how many quarters you should give customer
        int quarters = calculate_quarters(cents);

        // Subtract the value of those quarters from cents
        cents = cents - (quarters * 25);
    }

    int calculate_quarters(int cents)
    {
        // Calculate how many quarters you should give customer
        int quarters = 0;
        while (cents >= 25)
        {
            quarters++;
            cents = cents - 25;
        }
        return quarters;
    }

A few problems down, and a few more to go! Notice a pattern you could re-use here?

## How to Test

For this program, try testing your code manually. It’s good practice:

- If you input `-1`, does your program prompt you again?
- If you input `0`, does your program output `0`?
- If you input `1`, does your program output `1` (i.e., one penny)?
- If you input `4`, does your program output `4` (i.e., four pennies)?
- If you input `5`, does your program output `1` (i.e., one nickel)?
- If you input `24`, does your program output `6` (i.e., two dimes and four pennies)?
- If you input `25`, does your program output `1` (i.e., one quarter)?
- If you input `26`, does your program output `2` (i.e., one quarter and one penny)?
- If you input `99`, does your program output `9` (i.e., three quarters, two dimes, and four pennies)?

### Correctness

In your terminal, execute the below to check your work’s correctness.

    check50 cs50/problems/2024/x/cash

### Style

Execute the below to evaluate the style of your code using `style50`.

    style50 cash.c

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2024/x/cash
