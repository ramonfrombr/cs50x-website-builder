# Inheritance

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/xfZhb6lmxjk?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Problem to Solve

A person’s blood type is determined by two alleles (i.e., different forms of a gene). The three possible alleles are A, B, and O, of which each person has two (possibly the same, possibly different). Each of a child’s parents randomly passes one of their two blood type alleles to their child. The possible blood type combinations, then, are: OO, OA, OB, AO, AA, AB, BO, BA, and BB.

For example, if one parent has blood type AO and the other parent has blood type BB, then the child’s possible blood types would be AB and OB, depending on which allele is received from each parent. Similarly, if one parent has blood type AO and the other OB, then the child’s possible blood types would be AO, OB, AB, and OO.

In a file called `inheritance.c` in a folder called `inheritance`, simulate the inheritance of blood types for each member of a family.

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-J9DnbdokgIAjWUbzC2CBqP22N" src="https://asciinema.org/a/J9DnbdokgIAjWUbzC2CBqP22N.js"></script>

## Distribution Code

For this problem, you’ll extend the functionality of code provided to you by CS50’s staff.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2023/fall/psets/5/inheritance.zip

in order to download a ZIP called `inheritance.zip` into your codespace.

Then execute

    unzip inheritance.zip

to create a folder called `inheritance`. You no longer need the ZIP file, so you can execute

    rm inheritance.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd inheritance

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    inheritance/ $

Execute `ls` by itself, and you should see and see a file named `inheritance.c`.

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

## Implementation Details

Complete the implementation of `inheritance.c`, such that it creates a family of a specified generation size and assigns blood type alleles to each family member. The oldest generation will have alleles assigned randomly to them.

- The `create_family` function takes an integer (`generations`) as input and should allocate (as via `malloc`) one `person` for each member of the family of that number of generations, returning a pointer to the `person` in the youngest generation.
  - For example, `create_family(3)` should return a pointer to a person with two parents, where each parent also has two parents.
  - Each `person` should have `alleles` assigned to them. The oldest generation should have alleles randomly chosen (as by calling the `random_allele` function), and younger generations should inherit one allele (chosen at random) from each parent.
  - Each `person` should have `parents` assigned to them. The oldest generation should have both `parents` set to `NULL`, and younger generations should have `parents` be an array of two pointers, each pointing to a different parent.

## Hints

### Understand the code in `inheritance.c`

Take a look at the distribution code in `inheritance.c`.

Notice the definition of a type called `person`. Each person has an array of two `parents`, each of which is a pointer to another `person` struct. Each person also has an array of two `alleles`, each of which is a `char` (either `'A'`, `'B'`, or `'O'`).

    // Each person has two parents and two alleles
    typedef struct person
    {
        struct person *parents[2];
        char alleles[2];
    }
    person;

Now, take a look at the `main` function. The function begins by “seeding” (i.e., providing some initial input to) a random number generator, which we’ll use later to generate random alleles.

    // Seed random number generator
    srand(time(0));

The `main` function then calls the `create_family` function to simulate the creation of `person` structs for a family of 3 generations (i.e. a person, their parents, and their grandparents).

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

We then call `print_family` to print out each of those family members and their blood types.

    // Print family tree of blood types
    print_family(p, 0);

Finally, the function calls `free_family` to `free` any memory that was previously allocated with `malloc`.

    // Free memory
    free_family(p);

The `create_family` and `free_family` functions are left to you to write!
