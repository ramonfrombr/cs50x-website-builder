## Loops

### for

Whenever you need temporary variables for iteration, use `i`, then `j`, then `k`, unless more specific names would make your code more readable:

    for (int i = 0; i < LIMIT; i++)
    {
        for (int j = 0; j < LIMIT; j++)
        {
            for (int k = 0; k < LIMIT; k++)
            {
                // Do something
            }
        }
    }

If you need more than three variables for iteration, it might be time to rethink your design!

### while

Declare `while` loops as follows:

    while (condition)
    {
        // Do something
    }

Notice how:

- each curly brace is on its own line;
- there’s a single space after `while`;
- there isn’t any space immediately after the `(` or immediately before the `)`; and
- the loop’s body (a comment in this case) is indented with 4 spaces.

### do … while

Declare `do ... while` loops as follows:

    do
    {
        // Do something
    }
    while (condition);

Notice how:

- each curly brace is on its own line;
- there’s a single space after `while`;
- there isn’t any space immediately after the `(` or immediately before the `)`; and
- the loop’s body (a comment in this case) is indented with 4 spaces.

## Pointers

When declaring a pointer, write the `*` next to the variable, as in:

    int *p;

Don’t write it next to the type, as in:

    int* p;

## Variables

Because CS50 uses [C99](http://en.wikipedia.org/wiki/C99), do not define all of your variables at the very top of your functions but, rather, when and where you actually need them. Moreover, scope your variables as tightly as possible. For instance, if `i` is only needed for the sake of a loop, declare `i` within the loop itself:

    for (int i = 0; i < LIMIT; i++)
    {
        printf("%i\n", i);
    }

Though it’s fine to use variables like `i`, `j`, and `k` for iteration, most of your variables should be more specifically named. If you’re summing some values, for instance, call your variable `sum`. If your variable’s name warrants two words (e.g., `is_ready`), put an underscore between them, a convention popular in C though less so in other languages.

If declaring multiple variables of the same type at once, it’s fine to declare them together, as in:

    int quarters, dimes, nickels, pennies;

Just don’t initialize some but not others, as in:

    int quarters, dimes = 0, nickels = 0 , pennies;

Also take care to declare pointers separately from non-pointers, as in:

    int *p;
    int n;

Don’t declare pointers on the same line as non-pointers, as in:

    int *p, n;

## Structures

Declare a `struct` as a type as follows, with each curly brace on its own line and members indented therein, with the type’s name also on its own line:

    typedef struct
    {
        string name;
        string dorm;
    }
    student;

If the `struct` contains as a member a pointer to another such `struct`, declare the `struct` as having a name identical to the type, without using underscores:

    typedef struct node
    {
        int n;
        struct node *next;
    }
    node;
