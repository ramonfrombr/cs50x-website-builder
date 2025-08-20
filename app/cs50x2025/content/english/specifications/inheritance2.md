### Complete the `create_family` function

The `create_family` function should return a pointer to a `person` who has inherited their blood type from the number of `generations` given as input.

- Notice first that this problem poses a good opportunity for recursion.
  - To determine the present person’s blood type, you need to first determine their parents’ blood types.
  - To determine those parents’ blood types, you must first determine _their_ parents’ blood types. And so on until you reach the last generation you wish to simulate.

To solve this problem, you’ll find several TODOs in the distribution code.

First, you should allocate memory for a new person. Recall that you can use `malloc` to allocate memory, and `sizeof(person)` to get the number of bytes to allocate.

    // Allocate memory for new person
    person *new_person = malloc(sizeof(person));

Next, you should check if there are still generations left to create: that is, whether `generations > 1`.

If `generations > 1`, then there are more generations that still need to be allocated. We’ve already created two new parents, `parent0` and `parent1`, by recursively calling `create_family`. Your `create_family` function should then set the parent pointers of the new person you created. Finally, assign both `alleles` for the new person by randomly choosing one allele from each parent.

- Remember, to access a variable via a pointer, you can use arrow notation. For example, if `p` is a pointer to a person, then a pointer to this person’s first parent can be accessed by `p->parents[0]`.
- You might find the `rand()` function useful for randomly assigning alleles. This function returns an integer between `0` and `RAND_MAX`, or `32767`. In particular, to generate a pseudorandom number that is either `0` or `1`, you can use the expression `rand() % 2`.

  // Create two new parents for current person by recursively calling create_family
  person *parent0 = create_family(generations - 1);
  person *parent1 = create_family(generations - 1);

  // Set parent pointers for current person
  new_person->parents[0] = parent0;
  new_person->parents[1] = parent1;

  // Randomly assign current person's alleles based on the alleles of their parents
  new_person->alleles[0] = parent0->alleles[rand() % 2];
  new_person->alleles[1] = parent1->alleles[rand() % 2];

Let’s say there are no more generations left to simulate. That is, `generations == 1`. If so, there will be no parent data for this person. Both parents of your new person should be set to `NULL`, and each `allele` should be generated randomly.

    // Set parent pointers to NULL
    new_person->parents[0] = NULL;
    new_person->parents[1] = NULL;

    // Randomly assign alleles
    new_person->alleles[0] = random_allele();
    new_person->alleles[1] = random_allele();

Finally, your function should return a pointer for the `person` that was allocated.

    // Return newly created person
    return new_person;

### Complete the `free_family` function

The `free_family` function should accept as input a pointer to a `person`, free memory for that person, and then recursively free memory for all of their ancestors.

- Since this is a recursive function, you should first handle the base case. If the input to the function is `NULL`, then there’s nothing to free, so your function can return immediately.
- Otherwise, you should recursively `free` both of the person’s parents before `free`ing the child.

The below is quite the hint, but here’s how to do just that!

    // Free `p` and all ancestors of `p`.
    void free_family(person *p)
    {
        // Handle base case
        if (p == NULL)
        {
            return;
        }

        // Free parents recursively
        free_family(p->parents[0]);
        free_family(p->parents[1]);

        // Free child
        free(p);
    }

### Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/9p7ddI3ozTY?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

<details><summary>Not sure how to solve?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/H7LULatPwcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

## How to Test

Upon running `./inheritance`, your program should adhere to the rules described in the background. The child should have two alleles, one from each parent. The parents should each have two alleles, one from each of their parents.

For example, in the example below, the child in Generation 0 received an O allele from both Generation 1 parents. The first parent received an A from the first grandparent and a O from the second grandparent. Similarly, the second parent received an O and a B from their grandparents.

    $ ./inheritance
    Child (Generation 0): blood type OO
        Parent (Generation 1): blood type AO
            Grandparent (Generation 2): blood type OA
            Grandparent (Generation 2): blood type BO
        Parent (Generation 1): blood type OB
            Grandparent (Generation 2): blood type AO
            Grandparent (Generation 2): blood type BO

### Correctness

    check50 cs50/problems/2024/x/inheritance

### Style

    style50 inheritance.c

## How to Submit

    submit50 cs50/problems/2024/x/inheritance
